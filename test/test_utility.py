import rotate_ocr.utility.convert_coords as cc

def test_yolo_to_pixel_coords():
    x_center = 0.5
    y_center = 0.5
    width = 0.5
    height = 0.5
    img_width = 100
    img_height = 100

    result = cc.yolo_to_pixel_coords(x_center, y_center, width, height, img_width, img_height)

    assert result == ((25, 25), (75, 75))

def test_pixel_to_yolo_coords():
    x_left_top = 25
    y_left_top = 25
    x_right_bottom = 75
    y_right_bottom = 75
    img_width = 100
    img_height = 100

    result = cc.pixel_to_yolo_coords(x_left_top, y_left_top, x_right_bottom, y_right_bottom, img_width, img_height)

    assert result == (0.5, 0.5, 0.5, 0.5)

if __name__ == "__main__":
    test_yolo_to_pixel_coords()
    test_pixel_to_yolo_coords()
    print("All tests passed.")
