from PIL import Image
import numpy as np
from pathlib import Path

def rotate_img(input_file_path: str, output_file_path: str, angle: int):
    """
    画像を回転する（クロップせず、領域を拡張する）

    Parameters
    ----------
    input_file_path : str
        入力ファイルPath
    output_file_path : str
        出力ファイルPath
    angle : int
        回転角度
    """
    # 画像読み込み
    img = Image.open(input_file_path)
    w, h = img.size # 幅、高さ

    # 回転角の指定
    angle = angle % 360

    # 元画像の中心を軸に回転する
    # PillowではImage.rotateで中心を基準に回転できる
    # expand=Trueで回転後のサイズを自動調整
    img_rot = img.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)

    # 画像を保存
    img_rot.save(output_file_path)

def rotate_img_for_ocr(input_file_path: str, output_dir: str):
    """
    OCR用に45度ずつ回転させる

    Parameters
    ----------
    input_file_path : str
        入力ファイルPath
    output_dir : str
        出力ディレクトリPath

    Returns
    -------
    output_path_list : list
        出力ファイルPathのリスト
    """
    # ファイル名、拡張子を取得
    file_name = Path(input_file_path).stem
    file_ext = Path(input_file_path).suffix
    output_dir_path = Path(output_dir)

    # 出力ファイルPathのリスト
    output_path_list = []

    # 45度ずつ回転させる角度のリスト
    # TODO: 0度のみでテスト
    ## angle_list = [0, 45, 90, 135, 180, 225, 270, 315]
    angle_list = [0,]
    for angle in angle_list:
        # 出力ファイル名、Path
        output_file_name = f"{file_name}_{angle}{file_ext}"
        output_file_path = output_dir_path / output_file_name
        # print(output_file_path)

        # 画像を回転
        rotate_img(input_file_path, output_file_path, angle)

        # 出力ファイルPathをリストに追加
        output_path_list.append(output_file_path)

    return output_path_list

def open_img(input_file_path):
    """
    画像を開く

    Parameters
    ----------
    input_file_path : str
        入力ファイルPath

    Returns
    -------
    Image
        PIL.Imageオブジェクト
    """
    return Image.open(input_file_path)
