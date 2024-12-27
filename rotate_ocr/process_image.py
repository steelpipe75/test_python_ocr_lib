import os
import shutil
from pathlib import Path

import rotate_ocr.image_helper.rotate_img as rotate_img
import rotate_ocr.image_helper.image_size as image_size

import rotate_ocr.ocr_helper.pytesseract_helper as t_ocr
import rotate_ocr.ocr_helper.easy_ocr_helper as e_ocr
import rotate_ocr.ocr_helper.paddle_ocr_helper as p_ocr


def write_size_file(output_size_file_path, filename, size):
    if not os.path.exists(output_size_file_path):
        with open(output_size_file_path, "w") as f:
            f.write("filename,width,height\n")
    
    with open(output_size_file_path, "a") as f:
        f.write(f"{filename},{size[0]},{size[1]}\n")


def process_image(img_path, output_dir_path, mode, output_size_file_path):
    os.makedirs(output_dir_path, exist_ok=True)

    img_file_name = Path(img_path).stem

    size = image_size.get_image_size(img_path)
    write_size_file(output_size_file_path, img_file_name, size)

    rotate_img_path_list = rotate_img.rotate_img_for_ocr(img_path, output_dir_path)

    # OCR
    for rotate_img_path in rotate_img_path_list:
        print(f"Processing {rotate_img_path}")

        file_name = Path(rotate_img_path).stem
        file_ext = Path(rotate_img_path).suffix.replace(".", "")
        output_dir_path = Path(output_dir_path) / img_file_name / f"{file_name}_{file_ext}"

        os.makedirs(output_dir_path, exist_ok=True)

        # 画像ファイルのコピー
        move_img_path = output_dir_path / f"{file_name}.{file_ext}"
        shutil.move(rotate_img_path, move_img_path)

        if "t" in mode:
            # Tesseract OCR
            t_path = output_dir_path / f"tesseract_{file_name}.csv"
            t_helper = t_ocr.pyTesseractHelper()
            t_df = t_helper.ocr(move_img_path.as_posix())
            t_df.to_csv(t_path, index=False, encoding="cp932", errors="replace")

        if "e" in mode:
            # Easy OCR
            e_path = output_dir_path / f"easy_ocr_{file_name}.csv"
            e_helper = e_ocr.EasyOcrHelper()
            e_df = e_helper.ocr(move_img_path.as_posix())
            e_df.to_csv(e_path, index=False, encoding="cp932", errors="replace")

        if "p" in mode:
            # Paddle OCR
            p_path = output_dir_path / f"paddle_ocr_{file_name}.csv"
            p_helper = p_ocr.PaddleOcrHelper()
            p_df = p_helper.ocr(move_img_path.as_posix())
            p_df.to_csv(p_path, index=False, encoding="cp932", errors="replace")
