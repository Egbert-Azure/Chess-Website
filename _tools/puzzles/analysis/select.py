"""Pick the shortlist from the verified puzzles: one per game, a mix of kinds,
the most instructive first.
Usage: python3 -I select.py <verified.json> <out.json> [count]"""
import json, sys

ME = "Schroeer, Egbert"
items = [x for path in sys.argv[1].split(",") for x in json.load(open(path))]
COUNT = int(sys.argv[3]) if len(sys.argv) > 3 else 16


def mate_in(p):
    return (100_000 - p["deep1"]) // 100 if p["deep1"] >= 95_000 else None


def score(p):
    s = {"mate": 5, "win": 4, "save": 3}[p["kind"]]
    if p.get("whatif"):
        s = 3.5
    if p["kind"] == "save" and not p["me_to_move"]:
        s = 1.5
    if p["me_to_move"]:
        s += 1
    if any(k in p["event"] for k in ("Electronic Knights", "Palciauskas")):  # US Chess events: no engines
        s += 1.5  # played without engines: finding (or missing) the one move is a real human moment
    if p["sacrifice"]:
        s += 2
    elif p["quiet"]:
        s += 1
    if p["simple"]:
        s -= 3
    m = mate_in(p)
    if m == 1:
        s -= 4
    elif m and m > 5:
        s -= 3  # too long to solve comfortably; a later, shorter moment of the same attack is better
    if p["kind"] == "save":
        if p["deep2"] <= -95_000:
            s += 1  # every other move gets mated
        if not p["me_to_move"]:
            s -= 2
    return s


# within a game keep the start of each combination: drop positions that follow
# on from an earlier puzzle in the same game (same side, within 4 plies)
items.sort(key=lambda p: (p["game"], p["ply"]))
kept = []
for p in items:
    if (kept and kept[-1]["game"] == p["game"] and p["ply"] - kept[-1]["ply"] <= 4
            and not p.get("whatif") and p["kind"] != "mate"):
        continue
    kept.append(p)

kept = [p for p in kept if not p["simple"]]  # taking a piece that was left hanging is too easy
for p in kept:
    p["score"] = score(p)
best_per_game = {}
for p in sorted(kept, key=lambda p: -p["score"]):
    best_per_game.setdefault(p["game"], p)
ranked = sorted(best_per_game.values(), key=lambda p: -p["score"])

# keep the mix: at most a third defensive positions
MAX_SAVES = max(1, COUNT // 3)
picks, saves = [], 0
for p in ranked:
    if len(picks) >= COUNT:
        break
    if p["kind"] == "save":
        if saves >= MAX_SAVES:
            continue
        saves += 1
    picks.append(p)
json.dump(picks, open(sys.argv[2], "w"), indent=1)
print(f"{len(items)} verified, {len(kept)} after merging combinations, {len(ranked)} games, {len(picks)} picked")
for i, p in enumerate(picks, 1):
    kind = "what if" if p.get("whatif") else p["kind"]
    print(f"{i:2} {p['score']:4.1f} {kind:7} {p['to_move']:5} {p['solution_san']:8} {'sac ' if p['sacrifice'] else ''}{'quiet ' if p['quiet'] else ''}"
          f"{'found' if p['found'] else ('—' if p.get('whatif') else 'missed')} | {p['white'][:16]} – {p['black'][:16]} {p['result']} | {p['event'][:40]}")
