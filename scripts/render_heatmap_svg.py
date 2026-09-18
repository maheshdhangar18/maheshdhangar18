import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

with open("data/contributions.json") as f:
    days = json.load(f)

rects = []
for i, day in enumerate(days[-371:]):  # मागील 53 आठवडे
    col = i // 7
    row = i % 7
    x = col * 15 + 10
    y = row * 15 + 10
    color = PALETTE[day["level"]]
    delay = (col * 0.03) + (row * 0.01)
    rects.append(
        f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{color}" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{delay:.2f}s" fill="freeze" />'
        f'</rect>'
    )

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 125" width="820" height="125">
<rect width="100%" height="100%" fill="#0d1117" rx="6" />
{''.join(rects)}
</svg>'''

with open("contrib-heatmap.svg", "w") as f:
    f.write(svg_content)

print("Heatmap SVG created!")
