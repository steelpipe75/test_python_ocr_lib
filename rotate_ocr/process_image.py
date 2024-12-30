import os
import shutil
import json
from pathlib import Path

import rotate_ocr.image_helper.rotate_img as rotate_img
import rotate_ocr.image_helper.image_size as image_size
import rotate_ocr.image_helper.blackout_text_areas as bta

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


def ocr_processing(
        img_path : Path,
        degree : int,
        img_file_name : str,
        output_dir_path : Path,
        ocr_name_str : str,
        helper_class,
        size : tuple[int, int]
    ):
    helper = helper_class()

    print(f"# Processing | {ocr_name_str} : {img_path}")

    file_name = img_path.stem
    file_ext = img_path.suffix.replace(".", "")
    output_ocr_path = output_dir_path / ocr_name_str / img_file_name / f"{file_name}_{file_ext}"

    os.makedirs(output_ocr_path, exist_ok=True)

    output_base_path = output_ocr_path / f"{file_name}_{degree:03}.csv"
    rotate_img_path = output_ocr_path / f"{file_name}_{degree:03}.{file_ext}"

    rotate_img.rotate_img(
            img_path.as_posix(),
            rotate_img_path.as_posix(),
            degree
        )

    ocr_result = helper.ocr(rotate_img_path.as_posix())

    bta_image_path = output_ocr_path / f"{file_name}_{degree:03}_bta.{file_ext}"
    bta.blackout_text_areas(rotate_img_path, ocr_result, bta_image_path)

    converted_result = cort.convert_ocr_result_table(ocr_result, size)
    converted_result.to_csv(output_base_path, index=False, encoding="cp932", errors="replace")
    # ファイル名と拡張子を分割して "_utf8" を追加
    utf8_path = output_base_path.with_name(output_base_path.stem + "_utf8" + output_base_path.suffix)
    converted_result.to_csv(utf8_path, index=False, encoding="UTF-8", errors="replace")

    json_str = converted_result.to_json(orient="records", force_ascii=False)
    # print(json_str)

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

    return img_path

def process_image(img_path, output_dir_path, mode, output_size_file_path):
    os.makedirs(output_dir_path, exist_ok=True)

    img_file_name = Path(img_path).stem

    size = image_size.get_image_size(img_path)
    write_size_file(output_size_file_path, img_file_name, size)

    rotate = True if "r" in mode else False

    if rotate:
        rotate_deg_list = [0, 45, 90, 135, 180, 225, 270, 315]
    else:
        rotate_deg_list = [0]

    output_dir = Path(output_dir_path)

    pobj_img_path = Path(img_path)

    # Tesseract
    if "t" in mode:
        work_img_path = pobj_img_path
        for degree in rotate_deg_list:
            work_img_path = ocr_processing(
                    work_img_path,
                    degree,
                    img_file_name,
                    output_dir,
                    "tesseract",
                    t_ocr.pyTesseractHelper,
                    size
                )

    # EasyOCR
    if "e" in mode:
        work_img_path = pobj_img_path
        for degree in rotate_deg_list:
            work_img_path = ocr_processing(
                    work_img_path,
                    degree,
                    img_file_name,
                    output_dir,
                    "EasyOCR",
                    e_ocr.EasyOcrHelper,
                    size
                )

    # PaddleOCR
    if "p" in mode:
        work_img_path = pobj_img_path
        for degree in rotate_deg_list:
            work_img_path = ocr_processing(
                    work_img_path,
                    degree,
                    img_file_name,
                    output_dir,
                    "PaddleOCR",
                    p_ocr.PaddleOcrHelper,
                    size
                )
