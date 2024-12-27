import pandas as pd

import rotate_ocr.utility.convert_coords as cc


def convert_ocr_result_table(ocr_result_table: pd.DataFrame, image_size):
    x_center_list = []
    y_center_list = []
    width_list = []
    height_list = []
    
    for index, row in ocr_result_table.iterrows():
        print(f"Processing {index}")
        x_lt = row["座標(左上x)"]
        y_lt = row["座標(左上y)"]
        x_rb = row["座標(右下x)"]
        y_rb = row["座標(右下y)"]
        img_width = image_size[0]
        img_height = image_size[1]
        
        x_center, y_center, width, height = cc.pixel_to_yolo_coords(x_lt, y_lt, x_rb, y_rb, img_width, img_height)
        
        x_center_list.append(x_center)
        y_center_list.append(y_center)
        width_list.append(width)
        height_list.append(height)

    ocr_result_table["x_center"] = x_center_list
    ocr_result_table["y_center"] = y_center_list
    ocr_result_table["width"] = width_list
    ocr_result_table["height"] = height_list

    return ocr_result_table