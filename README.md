# test_python_ocr_lib

PythonのOCRライブラリの利用方法調査/精度確認

* [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
* [pytesseract](https://github.com/madmaze/pytesseract)
* [EasyOCR](https://github.com/JaidedAI/EasyOCR)

-----

## install

tesseractはあらかじめインストールしておいてください。

> [!NOTE]
> tesseract.exeへのPATHが通っている / もしくは下記3つのいずれかtesseract.exeがインストールされている前提の実装
> 
> * `"C:/Program Files/Tesseract-OCR/tesseract.exe"`  
> * `"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"`  
> * `"C:/Users/<ユーザー名>/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"`
> 
> 別のPathにインストールした場合は、 [pytesseract_helper.py](./rotate_ocr/pytesseract_helper.py) の `common_paths` に追加して下さい。


ソースをダウンロードしたフォルダで以下を実施
```
pip install -e .
```

-----

## 使い方

``` shell
python -m rotate_ocr 入力画像ファイルPath 出力フォルダPath
```
