from PIL import Image
from pathlib import Path

def get_image_size(input_file_path: str):
    """
    画像のサイズを取得する

    Parameters
    ----------
    input_file_path : str
        入力ファイルPath

    Returns
    -------
    size : tuple
        画像サイズ（幅、高さ）
    """
    # 画像読み込み
    img = Image.open(input_file_path)
    size = img.size # 幅、高さ

    return size