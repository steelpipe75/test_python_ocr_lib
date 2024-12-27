def yolo_to_pixel_coords(x_center, y_center, width, height, img_width, img_height):
    """
    YOLOのバウンディングボックス座標を画素単位の左上・右下の座標に変換する関数。

    Parameters:
        x_center (float): バウンディングボックスの中心のx座標（相対座標）。
        y_center (float): バウンディングボックスの中心のy座標（相対座標）。
        width (float): バウンディングボックスの幅（相対値）。
        height (float): バウンディングボックスの高さ（相対値）。
        img_width (int): 画像の幅（ピクセル数）。
        img_height (int): 画像の高さ（ピクセル数）。

    Returns:
        tuple: 左上 (x_left_top, y_left_top)、右下 (x_right_bottom, y_right_bottom) のピクセル座標。
    """
    # バウンディングボックスの幅と高さをピクセル単位に変換
    box_width = width * img_width
    box_height = height * img_height

    # 中心から各頂点を計算
    x_center_pixel = x_center * img_width
    y_center_pixel = y_center * img_height

    # 左上と右下の座標を計算
    x_left_top = x_center_pixel - box_width / 2
    y_left_top = y_center_pixel - box_height / 2
    x_right_bottom = x_center_pixel + box_width / 2
    y_right_bottom = y_center_pixel + box_height / 2

    return (int(x_left_top), int(y_left_top)), (int(x_right_bottom), int(y_right_bottom))

def pixel_to_yolo_coords(x_left_top, y_left_top, x_right_bottom, y_right_bottom, img_width, img_height):
    """
    ピクセル座標のバウンディングボックスをYOLO形式の座標に変換する関数。

    Parameters:
        x_left_top (int): 左上のx座標（ピクセル単位）。
        y_left_top (int): 左上のy座標（ピクセル単位）。
        x_right_bottom (int): 右下のx座標（ピクセル単位）。
        y_right_bottom (int): 右下のy座標（ピクセル単位）。
        img_width (int): 画像の幅（ピクセル数）。
        img_height (int): 画像の高さ（ピクセル数）。

    Returns:
        tuple: YOLO形式の (x_center, y_center, width, height)。
    """
    # 中心座標を計算
    x_center_pixel = (x_left_top + x_right_bottom) / 2
    y_center_pixel = (y_left_top + y_right_bottom) / 2

    # バウンディングボックスの幅と高さを計算
    box_width_pixel = x_right_bottom - x_left_top
    box_height_pixel = y_right_bottom - y_left_top

    # ピクセル座標を相対座標（0〜1）に変換
    x_center = x_center_pixel / img_width
    y_center = y_center_pixel / img_height
    width = box_width_pixel / img_width
    height = box_height_pixel / img_height

    return x_center, y_center, width, height
