from PIL import Image, ImageDraw
import pandas as pd

def blackout_text_areas(image_path, df, output_path, threshold = 0.7):
    """
    OCR結果をDataFrame形式で受け取り、文字検出箇所を黒い四角形で塗りつぶす関数。

    Args:
        image_path (str): 入力画像のファイルパス。
        df (pd.DataFrame): OCR結果のDataFrame。
        output_path (str): 塗りつぶし後の画像を保存するパス。

    Returns:
        None
    """
    # 画像を開く
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # DataFrameの各行から座標を取得して黒い四角形を描画
    for _, row in df.iterrows():
        if row['精度'] < threshold:
            # 精度が閾値未満の場合はスキップ
            continue

        # 座標を取得
        polygon = [
            (row['座標(左上x)'], row['座標(左上y)']),
            (row['座標(右上x)'], row['座標(右上y)']),
            (row['座標(右下x)'], row['座標(右下y)']),
            (row['座標(左下x)'], row['座標(左下y)'])
        ]

        # 四角形領域を黒で塗りつぶす
        draw.polygon(polygon, fill=(0, 0, 0))

    # 結果画像を保存
    image.save(output_path)
