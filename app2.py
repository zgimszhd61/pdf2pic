import fitz  # PyMuPDF
import io
from PIL import Image
import os

# PDF文件路径
pdf_path = '2406.19256v1.pdf'
# 输出图片的目录
output_dir = 'extracted_images'
# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 打开PDF文件
pdf_file = fitz.open(pdf_path)

# 遍历PDF的每一页
for page_index in range(len(pdf_file)):
    page = pdf_file[page_index]
    image_list = page.get_images(full=True)
    
    # 打印当前页的图片数量
    if image_list:
        print(f"[+] 在第 {page_index} 页找到 {len(image_list)} 张图片")
    else:
        print(f"[!] 第 {page_index} 页没有找到图片")
    
    # 遍历当前页的每一张图片
    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        
        # 保存图片
        image_filename = f"image_{page_index + 1}_{image_index}.{image_ext}"
        image_path = os.path.join(output_dir, image_filename)
        image.save(image_path)
        print(f"保存图片 {image_path}")