import os
import shutil
import json
from pathlib import Path

import rotate_ocr.image_helper.rotate_img as rotate_img
import rotate_ocr.image_helper.image_size as image_size

import rotate_ocr.utility.convert_ocr_result_table as cort

import rotate_ocr.ocr_helper.pytesseract_helper as t_ocr
import rotate_ocr.ocr_helper.easy_ocr_helper as e_ocr
import rotate_ocr.ocr_helper.paddle_ocr_helper as p_ocr


def write_size_file(output_size_file_path, filename, size):
    if not os.path.exists(output_size_file_path):
        with open(output_size_file_path, "w") as f:
            f.write("filename,width,height\n")
    
    with open(output_size_file_path, "a") as f:
        f.write(f"{filename},{size[0]},{size[1]}\n")


def ocr_processing(move_img_path, helper_class, output_base_path: Path, size):
    helper = helper_class()

    ocr_result = helper.ocr(move_img_path.as_posix())

    converted_result = cort.convert_ocr_result_table(ocr_result, size)
    converted_result.to_csv(output_base_path, index=False, encoding="cp932", errors="replace")

    json_str = converted_result.to_json(orient="records", force_ascii=False)
    print(json_str)

    json_obj = json.loads(json_str)
    ocr_obj = {
            "image_size": {
                    "witdh": size[0],
                    "height": size[1],
                },
            "ocr_result": json_obj,
        }

    with open(output_base_path.with_suffix(".json"), "w", encoding="utf-8") as f:
        json.dump(ocr_obj, f, ensure_ascii=False, indent=4)


def process_image(img_path, output_dir_path, mode, output_size_file_path):
    os.makedirs(output_dir_path, exist_ok=True)

    img_file_name = Path(img_path).stem

    size = image_size.get_image_size(img_path)
    write_size_file(output_size_file_path, img_file_name, size)

    rotate = True if "r" in mode else False

    if rotate:
        rotate_img_path_list = rotate_img.rotate_img_for_ocr(img_path, output_dir_path)
    else:
        rotate_img_path_list = [img_path]

    # OCR
    for rotate_img_path in rotate_img_path_list:
        print(f"Processing {rotate_img_path}")

        file_name = Path(rotate_img_path).stem
        file_ext = Path(rotate_img_path).suffix.replace(".", "")
        output_dir_path = Path(output_dir_path) / img_file_name / f"{file_name}_{file_ext}"

        os.makedirs(output_dir_path, exist_ok=True)

        # 画像ファイルの移動
        move_img_path = output_dir_path / f"{file_name}.{file_ext}"
        if rotate:
            shutil.move(rotate_img_path, move_img_path)
        else:
            shutil.copy(rotate_img_path, move_img_path)

        if "t" in mode:
            t_path = output_dir_path / f"tesseract_{file_name}.csv"
            ocr_processing(move_img_path, t_ocr.pyTesseractHelper, t_path, size)

        if "e" in mode:
            e_path = output_dir_path / f"easy_ocr_{file_name}.csv"
            ocr_processing(move_img_path, e_ocr.EasyOcrHelper, e_path, size)

        if "p" in mode:
            p_path = output_dir_path / f"paddle_ocr_{file_name}.csv"
            ocr_processing(move_img_path, p_ocr.PaddleOcrHelper, p_path, size)
