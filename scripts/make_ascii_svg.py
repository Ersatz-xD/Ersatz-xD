import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"
WIDTH = 80

def make_ascii():
    img = cv2.imread("source-prepped.png", cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    aspect = h / w
    new_h = int(WIDTH * aspect * 0.55)
    resized = cv2.resize(img, (WIDTH, new_h))
    
    svg_w, svg_h = 370, 380
    font_size = 7
    line_height = 8
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">',
        '<style>',
        '  text { font-family: monospace; font-size: 7px; fill: #c9d1d9; white-space: pre; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#0d1117"/>'
    ]
    
    for i, row in enumerate(resized):
        line = ""
        for pix in row:
            idx = int((255 - pix) / 255 * (len(RAMP) - 1))
            line += RAMP[idx]
        
        y = (i + 2) * line_height
        delay = round(i * 0.04, 2)
        
        # SMIL wipe animation per row
        svg.append(
            f'  <g clip-path="url(#clip_{i})">'
            f'<clipPath id="clip_{i}">'
            f'<rect x="0" y="{y-6}" width="0" height="{line_height}">'
            f'<animate attributeName="width" from="0" to="{svg_w}" dur="0.4s" begin="{delay}s" fill="freeze"/>'
            f'</rect>'
            f'</clipPath>'
            f'<text x="10" y="{y}">{line}</text>'
            f'</g>'
        )
        
    svg.append('</svg>')
    with open("avi-ascii.svg", "w") as f:
        f.write("\n".join(svg))
    print("Generated avi-ascii.svg")

if __name__ == "__main__":
    make_ascii()