import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep(input_path, output_path="source-prepped.png"):
    # 1. Remove Background
    print("Removing background...")
    input_img = Image.open(input_path)
    no_bg = remove(input_img)
    
    # 2. Composite onto pure white background
    white_bg = Image.new("RGBA", no_bg.size, (255, 255, 255, 255))
    white_bg.paste(no_bg, (0, 0), no_bg)
    gray = cv2.cvtColor(np.array(white_bg), cv2.COLOR_RGBA2GRAY)
    
    # 3. Apply CLAHE contrast boosting
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    cv2.imwrite(output_path, enhanced)
    print(f"Prepped photo saved to {output_path}")

if __name__ == "__main__":
    prep(sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg")
