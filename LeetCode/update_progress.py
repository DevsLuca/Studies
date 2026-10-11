import re

README = "README.md"

# Short labels for the roadmap graph (category number -> (node id, label))
NODES = {
    "01": ("AH", "Arrays and Hashing"), "02": ("TP", "Two Pointers"),
    "03": ("SW", "Sliding Window"),     "04": ("ST", "Stack"),
    "05": ("BS", "Binary Search"),      "06": ("LL", "Linked List"),
    "07": ("TR", "Trees"),              "08": ("HP", "Heap / Priority Queue"),
    "09": ("BT", "Backtracking"),       "10": ("TRI", "Tries"),
    "11": ("GP", "Graphs"),             "12": ("AG", "Advanced Graphs"),
    "13": ("DP1", "1-D DP"),            "14": ("DP2", "2-D DP"),
    "15": ("GR", "Greedy"),             "16": ("IN", "Intervals"),
    "17": ("MG", "Math and Geometry"),  "18": ("BM", "Bit Manipulation"),
}
EDGES = [("AH","TP"),("AH","ST"),("TP","BS"),("TP","SW"),("TP","LL"),("BS","TR"),
         ("LL","TR"),("TR","TRI"),("TR","HP"),("TR","BT"),("HP","IN"),("HP","GR"),
         ("HP","AG"),("BT","GP"),("BT","DP1"),("GP","AG"),("GP","DP2"),("DP1","DP2"),
         ("DP1","BM"),("DP2","MG"),("BM","MG")]


def parse_rows(body):
    """One dict per problem row: difficulty, LeetCode id, done?"""
    rows = []
    for line in body.splitlines():
        if not re.match(r'\|\s*\d+\s*\|', line):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        lc = re.search(r'LC(\d+)', cells[3])
        rows.append({"difficulty": cells[2],
                     "lc": lc.group(1) if lc else cells[1],
                     "done": "✅" in cells[4]})
    return rows


def bar(done, total, width=10):
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def pct(done, total):
    return round(100 * done / total) if total else 0


def replace_block(text, name, content):
    pattern = rf'(<!-- {name}:start -->).*?(<!-- {name}:end -->)'
    if not re.search(pattern, text, re.S):
        raise SystemExit(f"Missing <!-- {name}:start --> / <!-- {name}:end --> markers in {README}")
    return re.sub(pattern, lambda m: f"{m.group(1)}\n{content}\n{m.group(2)}", text, flags=re.S)


text = open(README, encoding="utf-8").read()
sections = re.findall(r'^## (\d+) (.+?)\n(.*?)(?=^## |\Z)', text, re.M | re.S)

cats, unique = [], {}
for num, name, body in sections:
    rows = parse_rows(body)
    cats.append((num, name, sum(r["done"] for r in rows), len(rows)))
    for r in rows:                                   # count each LeetCode problem once
        u = unique.setdefault(r["lc"], {"difficulty": r["difficulty"], "done": False})
        u["done"] = u["done"] or r["done"]

# 1. Progress table (per-category rows, unique-problem total)
total_done = sum(u["done"] for u in unique.values())
lines = ["| # | Category | Solved |", "|:-:|----------|:------:|"]
for num, name, done, total in cats:
    anchor = re.sub(r'[^\w\- ]', '', f"{num} {name}".lower()).replace(' ', '-')
    lines.append(f"| {num} | [{name}](#{anchor}) | {done} / {total} |")
lines.append(f"| | **Total (unique problems)** | **{total_done} / {len(unique)}** |")
text = replace_block(text, "progress", "\n".join(lines))

# 2. Roadmap graph (node colour: todo / doing / done)
g = ["```mermaid", "graph TD"]
for num, name, done, total in cats:
    node, label = NODES[num]
    state = "done" if total and done == total else "doing" if done else "todo"
    g.append(f'  {node}["{label}<br/>{done}/{total}"]:::{state}')
g.append("")
g += [f"  {a} --> {b}" for a, b in EDGES]
g += ["", "  classDef todo fill:#2b2b3a,stroke:#555,color:#ddd",
      "  classDef doing fill:#7a5c00,stroke:#d4a017,color:#fff",
      "  classDef done fill:#14532d,stroke:#22c55e,color:#fff", "```"]
text = replace_block(text, "graph", "\n".join(g))

# 3. Difficulty panel
d = ["| Difficulty | Solved | Total | Progress |", "|------------|:------:|:-----:|----------|"]
for level in ("Easy", "Medium", "Hard"):
    items = [u for u in unique.values() if u["difficulty"] == level]
    done = sum(u["done"] for u in items)
    d.append(f"| {level} | {done} | {len(items)} | {bar(done, len(items))} {pct(done, len(items))}% |")
d.append(f"| **Overall** | **{total_done}** | **{len(unique)}** | "
         f"{bar(total_done, len(unique))} {pct(total_done, len(unique))}% |")
text = replace_block(text, "difficulty", "\n".join(d))

open(README, "w", encoding="utf-8").write(text)
print(f"Updated: {total_done} / {len(unique)} unique problems solved")
