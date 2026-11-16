"""Restore accented names that ICCF's PGN lost, using the crosstables.
Usage: python3 -I fixnames.py <iccf-events.json> <puzzles.json>"""
import html, json, re, sys
pages = json.load(open(sys.argv[1]))
names = {html.unescape(m.group(1)).strip()
         for k, v in pages.items() if re.fullmatch(r"event-\d+", k)
         for m in re.finditer(r'player\?id=\d+[^>]*>([^<]+)<', v)}
items = json.load(open(sys.argv[2]))
for p in items:
    for side in ("white", "black"):
        n = p[side]
        if "�" in n:
            pat = re.compile("^" + re.escape(n).replace(re.escape("�"), ".") + "$")
            hits = [x for x in names if pat.match(x)]
            if len(hits) == 1:
                p[side] = hits[0]
json.dump(items, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
left = sum("�" in p["white"] + p["black"] for p in items)
print(f"names fixed; {left} still unreadable")
