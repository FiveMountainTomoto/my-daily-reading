import fitz
import os


def extract_page_range(file_path, start_page, end_page):
    """
    提取文件中的页码范围到新的pdf
    :param file_path: str - PDF文件的路径。
    :param start_page: int - 起始页码
    :param end_page: int - 终止页码
    """
    doc = fitz.open(file_path)
    output_doc = fitz.open()
    print(f'文件 "{os.path.basename(file_path)}" 打开成功！')

    for page_num in range(start_page - 1, end_page):
        output_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
    print(f'提取页码 {start_page} 到 {end_page} 页完成！')

    output_path = file_path.replace(".pdf", f"_extracted_{start_page}to{end_page}.pdf")
    output_doc.save(output_path)
    print(f'已保存到 "{output_path}" ')

    output_doc.close()
    doc.close()


def export_pdf_to_jpeg(pdf_path, dpi=300):
    """
    将PDF文件中的所有页面导出为JPEG格式的图片到文件路径下的output_pic文件夹。
    :param pdf_path: str - PDF文件的路径。
    :param dpi: int - 输出图片的分辨率（DPI），默认为300
    """
    # 打开文件
    doc = fitz.open(pdf_path)
    # 设置图片的输出分辨率（DPI）
    mat = fitz.Matrix(dpi / 72, dpi / 72)  # 72 DPI是PDF的默认分辨率
    # 文件名和输出路径
    filename = os.path.basename(pdf_path)
    init_path = os.path.dirname(pdf_path)
    output_path = os.path.join(init_path, 'output_pic')
    print(f'文件 "{filename}" 打开成功！')
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # 遍历pdf所有页面,导出图片
    file_len = len(doc)
    for page_num in range(file_len):
        print(f'正在导出第{page_num + 1}/{file_len}页...')
        page = doc[page_num]
        pix = page.get_pixmap(matrix=mat)
        # 保存图片为JPEG格式
        output_image_path = f"{output_path}/{filename}_page_{page_num + 1}.jpg"
        pix.save(output_image_path)
    print('导出图片完成!')
