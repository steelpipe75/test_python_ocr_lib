import pandas as pd
import easyocr


class EasyOcrHelper:
    def __init__(self, lang_list =["en", "ja"]):
        self.__easyocr_Reader = easyocr.Reader(
                lang_list=lang_list,
                verbose=False,
            )
        pass

    def ocr(self, img_path: str):
        print(img_path)
        data = self.__easyocr_Reader.readtext(img_path)

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
                    "文字列": datum[1],
                    "精度": datum[2],
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
