"""Builds _data/tournaments.yml, the data behind the Tournaments page, from
ICCF pages saved in the browser with iccf-snippet.js (see README.md).

Usage, from the Chess-Website folder:
    python3 _tools/tournaments/build.py ~/Downloads/iccf-events.json [more.json ...]

Needs only Python 3, nothing to install. Tournaments ICCF doesn't know about
(the 2021 Electronic Knights sections played on the US Chess server) come from
manual.json next to this script.
"""
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ME_ID, ME = "518240", "Schroeer, Egbert"
HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "_data" / "tournaments.yml"

# Names ICCF only knows by a code
NAMES = {
    "93278": "2021 Victor Palciauskas Tournament (21VP04)",
    "99566": "Web Server Category Tournament WS/CCE/A/30",
}
STAGES = {"": ("Preliminary", 1), "s": ("Semi-Final", 2), "f": ("Final", 3)}


def text(fragment):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment))).strip()


def points(value):
    """'5.5' or '5½' -> 5.5"""
    value = value.replace("½", ".5").strip()
    if value.startswith("."):
        value = "0" + value
    try:
        return float(value)
    except ValueError:
        return None


def show(score):
    """5.5 -> '5½', 0.5 -> '½', 3.0 -> '3'"""
    whole, half = int(score), score % 1 >= 0.5
    return ("" if whole == 0 and half else str(whole)) + ("½" if half else "")


def crosstable(page):
    i = page.find("<table id='crosstable'")
    if i < 0:
        return []
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", page[i:page.find("</table>", i)], re.S)
    head = [text(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", rows[1], re.S)]
    labels = [h for h in head[1:] if not h.isdigit()]
    players = []
    for row in rows[2:]:
        pid = re.search(r"player\?id=(\d+)", row)
        cells = [text(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
        if not pid or len(cells) < len(labels) + 5:
            continue
        results = [c for c in cells[7:-len(labels)] if c in ("0", "½", "1")]
        players.append({"id": pid.group(1), "title": cells[3], "name": cells[4],
                        "rating": cells[5].replace("P", "").strip(), "results": results,
                        **dict(zip(labels, cells[-len(labels):]))})
    return players


def iso(stamp):
    y, m, d = (int(x) for x in stamp.split("."))
    return date(y, m, d)


def event(eid, page, pgn):
    start = page.find('<div class="breadcrumb">')
    crumb = text(page[start:page.find("<img", start)]).replace("Home > Tables and results > ", "")
    parts = [p.strip() for p in crumb.split(">")]
    players = crosstable(page)
    me = next((p for p in players if p["id"] == ME_ID), None)
    if me is None:
        return None

    # my games: results and dates from the event's PGN
    wins = draws = losses = left = 0
    my_last, starts = [], []
    for game in re.split(r"(?=\[Event )", pgn.replace("\r", "")):
        if '[White "' not in game:
            continue
        starts += re.findall(r'\[Date "(\d{4}\.\d\d\.\d\d)"\]', game)
        white = re.search(r'\[White "([^"]*)"\]', game).group(1)
        black = re.search(r'\[Black "([^"]*)"\]', game).group(1)
        if ME not in (white, black):
            continue
        result = re.search(r'\[Result "([^"]*)"\]', game).group(1)
        if result == "1/2-1/2":
            draws += 1
        elif result in ("1-0", "0-1"):
            if (result == "1-0") == (white == ME):
                wins += 1
            else:
                losses += 1
        else:
            left += 1
        stamps = re.findall(r"%ccsnt (\d{4}\.\d\d\.\d\d)", game)
        if stamps:
            my_last.append(max(stamps))

    score = wins + draws / 2
    listed = points(me.get("Score", ""))
    if listed is not None and abs(listed - score) > 0.01:
        print(f"  note: event {eid}: crosstable says {me['Score']}, games add up to {show(score)}")
    played = wins + draws + losses
    e = {
        "iccf": int(eid),
        "status": "running" if left else "finished",
        "start": iso(min(starts)) if starts else None,
        "end": iso(max(my_last)) if my_last and not left else None,
        "games": played + left,
        "played": played,
        "left": left,
        "score": show(score),
        "points": score,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "place": int(me["Place"]) if me.get("Place", "").isdigit() and not left else None,
        "players": len(players),
        "rating": int(me["rating"]) if me["rating"].isdigit() else None,
        "title": me["title"] or None,
    }
    ek = re.search(r"\b(\d\d)EN([sf]?)(\d\d)\b", crumb)
    board = re.fullmatch(r"Board (\d+)", parts[-1])
    if ek:
        stage, order = STAGES[ek.group(2)]
        e.update(group="ek", section=ek.group(0), cycle=2000 + int(ek.group(1)), stage=stage, stage_order=order,
                 name=f"Electronic Knights {2000 + int(ek.group(1))} {stage}")
    elif board:
        # a friendly match board is a two-player match; a Champions League board is a group
        opp = e["games"] - score if not left and len(players) == 2 else None
        e.update(group="team", name=parts[0].replace(" - ", " – "), board=int(board.group(1)),
                 result=f"{show(score)}–{show(opp)}" if opp is not None else None)
        if opp is not None:
            e["place"] = None
    else:
        name = NAMES.get(eid) or (" ".join(parts) if parts[-1].isdigit() else ", ".join(parts))
        e.update(group="tournament", name=re.sub(r"^VWC\d+, ", "", name))
    return e


def load(paths):
    pages = {}
    for path in paths:
        pages.update(json.loads(Path(path).expanduser().read_text(encoding="utf-8")))
    return pages


def yaml_value(v):
    if v is None:
        return "null"
    if isinstance(v, (bool, int, float, date)):
        return str(v).lower() if isinstance(v, bool) else str(v)
    return json.dumps(v, ensure_ascii=False)


def main(paths):
    pages = load(paths)
    events = []
    for key in sorted(k for k in pages if re.fullmatch(r"event-\d+", k)):
        eid = key.split("-")[1]
        e = event(eid, pages[key], pages.get(f"{key}-games-1", ""))
        if e:
            events.append(e)
    known = {e.get("section") for e in events}
    for e in json.loads((HERE / "manual.json").read_text(encoding="utf-8")):
        if e.get("section") not in known:
            e["start"] = date.fromisoformat(e["start"]) if e.get("start") else None
            e.setdefault("end", None)
            events.append(e)
    events.sort(key=lambda e: (e["start"] or date.min, e.get("name", "")), reverse=True)
    for e in events:
        if e["group"] == "ek":  # Electronic Knights in championship order: cycle, round, section
            e["key"] = f'{e["cycle"]}-{e["stage_order"]}-{e["section"]}'

    latest = next(e for e in events if e.get("rating"))
    title = next((e["title"] for e in events if e.get("title")), "")
    order = ["name", "group", "section", "cycle", "stage", "stage_order", "board", "iccf", "status", "start", "end",
             "games", "played", "left", "score", "points", "wins", "draws", "losses", "result", "place", "players",
             "rating", "note", "key"]
    lines = ["# Made by _tools/tournaments/build.py from ICCF pages; see _tools/tournaments/README.md.",
             "# Edit manual.json there for tournaments ICCF doesn't list, then run the script again.",
             f"updated: {date.today()}",
             "player:",
             f"  title: {yaml_value(title)}",
             f"  rating: {latest['rating']}",
             f"  iccf: {ME_ID}",
             "events:"]
    for e in events:
        keys = [k for k in order if k in e and e[k] is not None]
        for n, k in enumerate(keys):
            lines.append(("  - " if n == 0 else "    ") + f"{k}: {yaml_value(e[k])}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    running = sum(e["status"] == "running" for e in events)
    print(f"Wrote {OUT.relative_to(OUT.parent.parent)}: {len(events)} tournaments, {running} running.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
