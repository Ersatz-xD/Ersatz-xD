import os

def make_card():
    static_mode = os.environ.get("STATIC", "0") == "1"
    svg_w, svg_h = 490, 380
    lines = [
        ("OS", "Manjaro Linux x86_64 [KDE Plasma]"),
        ("Role", "Full Stack Dev & ML Engineer"),
        ("Edu", "CS @ COMSATS University Islamabad"),
        ("Stack", "Python, React, Laravel, Flutter, Node"),
        ("AI / ML", "TensorFlow, PyTorch, LangChain, Gemini"),
        ("Location", "Karachi / Islamabad, Pakistan"),
        ("Contact", "ayaan@example.com")  # Update with your real email
    ]
    
    # Generate dedicated CSS classes for each row so GitHub doesn't strip inline styles
    style_rules = [
        "  .key { font-family: monospace; font-size: 14px; font-weight: bold; fill: #10b981; }",
        "  .val { font-family: monospace; font-size: 14px; fill: #c9d1d9; }",
        "  .title { font-family: monospace; font-size: 16px; font-weight: bold; fill: #34d399; }"
    ]
    
    if not static_mode:
        style_rules.append("  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }")
        for i in range(len(lines)):
            delay = round((i + 1) * 0.15, 2)
            style_rules.append(
                f"  .row-{i} {{ opacity: 0; animation: fadeIn 0.5s ease-forward {delay}s forwards; }}"
            )
            # Fallback standard syntax for webkit/GitHub SVG rendering
            style_rules.append(
                f"  .row-{i} {{ opacity: 0; animation: fadeIn 0.5s {delay}s forwards; }}"
            )
    else:
        for i in range(len(lines)):
            style_rules.append(f"  .row-{i} {{ opacity: 1; }}")
            
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">',
        "<style>",
        "\n".join(style_rules),
        "</style>",
        '<rect width="100%" height="100%" fill="#0d1117" rx="8"/>',
        '<text x="25" y="40" class="title">Ayaan@comsats ~ $ neofetch</text>',
        '<line x1="25" y1="50" x2="465" y2="50" stroke="#30363d" stroke-width="1"/>'
    ]
    
    for i, (k, v) in enumerate(lines):
        y = 95 + (i * 38)
        svg.append(
            f'  <g class="row-{i}">'
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