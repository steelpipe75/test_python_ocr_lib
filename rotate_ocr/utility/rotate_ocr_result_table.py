import pandas as pd
import numpy as np

import pandas as pd
import numpy as np


def rotate_ocr_result_table(
            df: pd.DataFrame,
            degree: int,
            rotated_size: tuple[int, int]
        ):
    """
    回転後の座標を回転前の元の画像座標に変換する。

    Parameters:
        df (pd.DataFrame): 座標情報を含むDataFrame。
        degree (float): 回転角度（時計回りが正）。
        rotated_size (tuple): 回転後の画像のサイズ (幅, 高さ)。

    Returns:
        pd.DataFrame: 回転前の座標が追加されたDataFrame。
    """
    # 回転後の画像の幅と高さ
    rotated_width, rotated_height = rotated_size

    # 回転後の画像の中心座標
    center_x, center_y = rotated_width / 2, rotated_height / 2

    # ラジアンに変換
    radian = np.deg2rad(-degree)  # 逆回転のため符号を反転

    # 回転行列を計算
    rotation_matrix = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)]
    ])

    # 座標を逆回転して新しい列を作成
    for corner in ["左上", "右上", "右下", "左下"]:
        original_x = []
        original_y = []
        for _, row in df.iterrows():
            x, y = row[f"座標({corner}x)"], row[f"座標({corner}y)"]
            # 平行移動（原点を中心にする）
            x -= center_x
            y -= center_y
            # 逆回転
            rotated = np.dot(rotation_matrix, np.array([x, y]))
            # 平行移動を戻す
            original_x.append(rotated[0] + center_x)
            original_y.append(rotated[1] + center_y)
        # 新しい列に追加
        df[f"元の座標({corner}x)"] = original_x
        df[f"元の座標({corner}y)"] = original_y

    return df
