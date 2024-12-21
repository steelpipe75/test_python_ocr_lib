# test_python_ocr_lib

PythonのOCRライブラリの利用方法調査/精度確認

* [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
* [pytesseract](https://github.com/madmaze/pytesseract)
* [EasyOCR](https://github.com/JaidedAI/EasyOCR)

-----

## install

ソースをダウンロードしたフォルダで以下を実施
```
pip install -e .
```

-----

## 使い方

``` shell
python -m rotate_ocr 入力画像ファイルPath 出力フォルダPath
```
