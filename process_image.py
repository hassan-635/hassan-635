import sys
import subprocess
import base64
import os
from io import BytesIO

def ensure_deps():
    try:
        from PIL import Image
        import rembg
    except ImportError:
        print("Installing Pillow and rembg...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "rembg", "onnxruntime"])
        from PIL import Image
        import rembg
    return Image, rembg

Image, rembg = ensure_deps()

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "myimage.jpeg")
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return
        
    print("Processing image with rembg...")
    
    # Read the image
    with open(input_path, "rb") as f:
        input_data = f.read()
        
    # Remove background
    output_data = rembg.remove(input_data)
    
    # Open as PIL Image
    transparent_img = Image.open(BytesIO(output_data)).convert("RGBA")
    
    # Resize for better quality but smaller size
    max_height = 600
    ratio = max_height / float(transparent_img.size[1])
    new_width = int((float(transparent_img.size[0]) * float(ratio)))
    banner_img = transparent_img.resize((new_width, max_height), Image.Resampling.LANCZOS)
    
    banner_buffer = BytesIO()
    banner_img.save(banner_buffer, format="PNG")
    banner_b64 = base64.b64encode(banner_buffer.getvalue()).decode('utf-8')
    
    # Crop for face. Head is at top center roughly.
    w, h = banner_img.size
    face_size = int(w * 0.45)
    left = (w - face_size) // 2
    top = int(h * 0.05)
    right = left + face_size
    bottom = top + face_size
    
    face_img = banner_img.crop((left, top, right, bottom))
    face_img = face_img.resize((150, 150), Image.Resampling.LANCZOS)
    
    face_buffer = BytesIO()
    face_img.save(face_buffer, format="PNG")
    face_b64 = base64.b64encode(face_buffer.getvalue()).decode('utf-8')
    
    with open(os.path.join(base_dir, "banner_b64.txt"), "w") as f:
        f.write(banner_b64)
        
    with open(os.path.join(base_dir, "face_b64.txt"), "w") as f:
        f.write(face_b64)
        
    print("Done! High quality Base64 files generated.")

if __name__ == "__main__":
    main()

