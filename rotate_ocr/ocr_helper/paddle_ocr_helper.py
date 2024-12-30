from paddleocr import PaddleOCR
import pandas as pd


class PaddleOcrHelper:
    def __init__(self, lang: str ="japan"):
        self.__paddle_ocr = PaddleOCR(lang=lang)
        pass

    def ocr(self, img_path: str):
        result = self.__paddle_ocr.ocr(img_path)

        data = result[0]

        result_array = []

        try:
            for datum in data:
                # print(datum)
                result_dict = {
                    "座標(左上x)":   datum[0][0][0],
                    "座標(左上y)":   datum[0][0][1],
                    "座標(右上x)":   datum[0][1][0],
                    "座標(右上y)":   datum[0][1][1],
                    "座標(右下x)":   datum[0][2][0],
                    "座標(右下y)":   datum[0][2][1],
                    "座標(左下x)":   datum[0][3][0],
                    "座標(左下y)":   datum[0][3][1],
                    "文字列": datum[1][0],
                    "精度": datum[1][1],
                }
                result_array.append(result_dict)

                result_df = pd.DataFrame(result_array)
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            columns = [
                "座標(左上x)",
                "座標(左上y)",
                "座標(右上x)",
                "座標(右上y)",
                "座標(右下x)",
                "座標(右下y)",
                "座標(左下x)",
                "座標(左下y)",
                "文字列",
                "精度",
            ]
            result_df = pd.DataFrame(columns=columns)

        return result_df
