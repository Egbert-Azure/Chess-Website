"""Collect Egbert's finished games: ICCF downloads plus the annotated 2021 US
Chess games on the site. Games from tournaments still running are left out.
Usage: python3 -I collect.py <iccf-events.json> <tournaments.yml> <repo> <out.pgn>"""
import io, json, re, sys
from pathlib import Path
import chess.pgn

ME = "Schroeer, Egbert"
pages = json.load(open(sys.argv[1]))
yml = open(sys.argv[2]).read()
repo, out = Path(sys.argv[3]), sys.argv[4]

running = set()
for block in yml.split("\n  - ")[1:]:
    iccf = re.search(r"^\s*iccf: (\d+)", block, re.M)
    if iccf and re.search(r'^\s*status: "running"', block, re.M):
        running.add(iccf.group(1))
names = {}
for block in yml.split("\n  - ")[1:]:
    iccf = re.search(r"^\s*iccf: (\d+)", block, re.M)
    name = re.search(r'^\s*name: (".*")$', block, re.M)
    sec = re.search(r'^\s*section: "([^"]*)"', block, re.M)
    if iccf:
        names[iccf.group(1)] = json.loads(name.group(1)) + (f" ({sec.group(1)})" if sec else "")

games, skipped_running, skipped_open = [], 0, 0
seen = set()
for key in sorted(k for k in pages if re.fullmatch(r"event-\d+-games-\d+", k)):
    eid = key.split("-")[1]
    stream = io.StringIO(pages[key].replace("\r", ""))
    while (g := chess.pgn.read_game(stream)) is not None:
        if ME not in (g.headers.get("White"), g.headers.get("Black")):
            continue
        if eid in running:
            skipped_running += 1
            continue
        if g.headers.get("Result") not in ("1-0", "0-1", "1/2-1/2"):
            skipped_open += 1
            continue
        ident = (g.headers["White"], g.headers["Black"], g.headers.get("Date"))
        if ident in seen:
            continue
        seen.add(ident)
        g.headers["Source"] = f"https://www.iccf.com/event?id={eid}"
        g.headers["SiteEvent"] = re.sub(r'"([^"]*)"', "“\\1”", names.get(eid, g.headers.get("Event", "")))
        games.append(g)

# 2021 Electronic Knights games on the US Chess server, from the site's game pages
us = 0
for page in sorted((repo / "_tournaments").glob("*.md")):
    text = page.read_text(encoding="utf-8")
    sec = re.search(r"^section:\s*(\S+)", text, re.M)
    if not sec or sec.group(1) not in ("21EN09", "21EN15", "21ENs03", "21ENs04"):
        continue  # only the sections played on the US Chess server; the rest come from ICCF
    for block in re.findall(r"```pgn\n(.*?)\n```", text, re.S):
        g = chess.pgn.read_game(io.StringIO(block))
        if not g or ME not in (g.headers.get("White"), g.headers.get("Black")):
            continue
        if g.headers.get("Result") not in ("1-0", "0-1", "1/2-1/2"):
            continue
        ident = (g.headers["White"], g.headers["Black"], g.headers.get("Date"))
        names_only = {(a, b) for a, b, _ in seen}
        if ident in seen or (g.headers["White"], g.headers["Black"]) in names_only:
            continue
        seen.add(ident)
        g.headers["Source"] = f"site:{page.name}"
        g.headers["SiteEvent"] = f"Electronic Knights 2021 ({sec.group(1)})"
        # keep only the main line: comments and variations aren't needed for the scan
        clean = chess.pgn.Game()
        clean.headers.update(g.headers)
        node = clean
        for mv in g.mainline_moves():
            node = node.add_main_variation(mv)
        games.append(clean)
        us += 1

with open(out, "w") as f:
    for g in games:
        print(g.accept(chess.pgn.StringExporter(headers=True, variations=False, comments=False)), file=f, end="\n\n")
res = {}
for g in games:
    r = g.headers["Result"]
    me_white = g.headers["White"] == ME
    k = "draw" if r == "1/2-1/2" else ("win" if (r == "1-0") == me_white else "loss")
    res[k] = res.get(k, 0) + 1
print(f"{len(games)} finished games ({us} from the 2021 US Chess pages); left out: {skipped_running} from running tournaments, {skipped_open} unfinished")
print("results:", res, "| running events:", sorted(running))
