import json

# Nightwing Blue Palette: Background -> Brightest Electric Cyan
PALETTE = ["#161b22", "#0a2540", "#004d80", "#0077b6", "#0096c7", "#00d9ff"]

def render_svg():
    with open("data/contributions.json") as f:
        data = json.load(f)["days"]
        
    svg_w, svg_h = 860, 160
    box_size = 11
    gap = 3
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">',
        '<style>',
        '  rect.day { opacity: 0; animation: slideDown 0.4s forwards; }',
        '  @keyframes slideDown { from { opacity: 0; transform: translateY(-5px); } to { opacity: 1; transform: translateY(0); } }',
        '</style>',
        '<rect width="100%" height="100%" fill="#0d1117" rx="6"/>',
        '<g transform="translate(20, 20)">'
    ]
    
    for i, day in enumerate(data[-371:]): # last 53 weeks
        col = i // 7
        row = i % 7
        x = col * (box_size + gap)
        y = row * (box_size + gap)
        color = PALETTE[day["level"]]
        delay = round((col + row) * 0.015, 2)
        
        svg.append(
            f'  <rect class="day" x="{x}" y="{y}" width="{box_size}" height="{box_size}" '
            f'rx="2" fill="{color}" style="animation-delay: {delay}s;"/>'
        )
        
    svg.append('</g></svg>')
    with open("contrib-heatmap.svg", "w") as f:
        f.write("\n".join(svg))
    print("Generated contrib-heatmap.svg")

if __name__ == "__main__":
    render_svg()