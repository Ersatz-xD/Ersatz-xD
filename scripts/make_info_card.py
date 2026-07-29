def make_card():
    svg_w, svg_h = 490, 380
    lines = [
        ("OS", "Manjaro Linux"),
        ("Role", "Full Stack Dev &amp; ML Engineer"),
        ("Edu", "CS @ COMSATS University Islamabad"),
        ("Stack", "Python, React, Laravel, Flutter, Node"),
        ("AI / ML", "TensorFlow, PyTorch, LangChain, Gemini"),
        ("Location", "Karachi / Islamabad, Pakistan"),
        ("Contact", "ayaan@example.com")  # Update with your real email
    ]
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">',
        "<style>",
        "  .key { font-family: monospace; font-size: 14px; font-weight: bold; fill: #10b981; }",
        "  .val { font-family: monospace; font-size: 14px; fill: #c9d1d9; }",
        "  .title { font-family: monospace; font-size: 16px; font-weight: bold; fill: #34d399; }",
        "</style>",
        '<rect width="100%" height="100%" fill="#0d1117" rx="8"/>',
        '<text x="25" y="40" class="title">Ayaan@comsats ~ $ neofetch</text>',
        '<line x1="25" y1="50" x2="465" y2="50" stroke="#30363d" stroke-width="1"/>'
    ]
    
    for i, (k, v) in enumerate(lines):
        y = 95 + (i * 38)
        delay = round((i + 1) * 0.15, 2)
        svg.append(
            f'  <g clip-path="url(#card_clip_{i})">'
            f'<clipPath id="card_clip_{i}">'
            f'<rect x="0" y="{y-18}" width="0" height="24">'
            f'<animate attributeName="width" from="0" to="{svg_w}" dur="0.4s" begin="{delay}s" fill="freeze"/>'
            f'</rect>'
            f'</clipPath>'
            f'<text x="25" y="{y}" class="key">{k}:</text>'
            f'<text x="125" y="{y}" class="val">{v}</text>'
            f'</g>'
        )
        
    svg.append("</svg>")
    with open("info-card.svg", "w") as f:
        f.write("\n".join(svg))
    print("Generated info-card.svg")

if __name__ == "__main__":
    make_card()