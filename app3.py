import fitz  # PyMuPDF

def find_non_text_areas(pdf_path):
    # 打开PDF文件
    doc = fitz.open(pdf_path)
    
    non_text_areas = []

    # 遍历每一页
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # 获取页面上的所有块
        blocks = page.get_text("blocks")
        
        # 遍历所有块，找出非文本块
        for block in blocks:
            x0, y0, x1, y1, block_type, _, _ = block
            if block_type != 0:  # 非文本块
                non_text_areas.append({
                    "page": page_num,
                    "bbox": (x0, y0, x1, y1)
                })
    
    return non_text_areas

# 示例使用
pdf_path = "2406.19256v1.pdf"
non_text_areas = find_non_text_areas(pdf_path)
for area in non_text_areas:
    print(f"Page: {area['page']}, BBox: {area['bbox']}")