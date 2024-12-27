from yomitoku import DocumentAnalyzer
from yomitoku.data.functions import load_image
import pandas as pd
import tempfile

class YomiTokuHelper:
    def __init__(self):
        self.__analyzer = DocumentAnalyzer(configs={}, visualize=False)
        pass

    def ocr(self, img_path: str):
        img = load_image(img_path)
        result, _, _ = self.__analyzer(img)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
            result.to_csv(temp_file_path)
            data = pd.read_csv(temp_file_path)

        return data
