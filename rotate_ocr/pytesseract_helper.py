import shutil
from PIL import Image
import pytesseract
import pandas as pd
from io import StringIO
import os

# sudo apt-get -y install tesseract-ocr tesseract-ocr-jpn
pytesseract.pytesseract.tesseract_cmd = None

class pyTesseractHelper:
    def __init__(self, tesseract_path = None, lang: str = "jpn+eng"):
        if pytesseract.pytesseract.tesseract_cmd is None:
            self._set_tesseract_path(tesseract_path)

        self.__lang = lang
        pass

    def ocr(self, img_path: str):
        result = pytesseract.pytesseract.image_to_data(
                            image=Image.open(img_path),
                            lang=self.__lang,
                        )

        df = pd.read_csv(StringIO(result), sep='\t')

        filtered_df = df[df["conf"] >= 0]

        filtered_df["文字列"] = filtered_df["text"]
        filtered_df["精度"] = filtered_df["conf"] / 100
        filtered_df["座標(左上x)"] = filtered_df["left"]
        filtered_df["座標(左上y)"] = filtered_df["top"]
        filtered_df["座標(右上x)"] = filtered_df["left"] + filtered_df["width"]
        filtered_df["座標(右上y)"] = filtered_df["top"]
        filtered_df["座標(右下x)"] = filtered_df["left"] + filtered_df["width"]
        filtered_df["座標(右下y)"] = filtered_df["top"] + filtered_df["height"]
        filtered_df["座標(左下x)"] = filtered_df["left"]
        filtered_df["座標(左下y)"] = filtered_df["top"] + filtered_df["height"]

        filtered_df = filtered_df[
                            [
                                "座標(左上x)", "座標(左上y)",
                                "座標(右上x)", "座標(右上y)",
                                "座標(右下x)", "座標(右下y)",
                                "座標(左下x)", "座標(左下y)",
                                "文字列",
                                "精度"
                            ]
                        ]

        return filtered_df

    def _find_tesseract_binary(self) -> str:
        if os.name == 'nt':
            # windows
            user_name = os.getlogin()  # ユーザー名を取得
            return f"C:/Users/{user_name}/AppData/Local/Programs/Tesseract-OCR/tesseract.exe" # デフォルトインストール先
        else:
            # not windows
            return shutil.which("tesseract")

    def _set_tesseract_path(self, tesseract_path: str):
        if tesseract_path is None:
            pytesseract.pytesseract.tesseract_cmd = self._find_tesseract_binary()
            # print(tesseract_path)
        else:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            # print(tesseract_path)
