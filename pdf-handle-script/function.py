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
