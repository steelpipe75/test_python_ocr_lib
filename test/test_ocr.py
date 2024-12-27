import rotate_ocr.image_helper.rotate_img as rotate_img
import rotate_ocr.ocr_helper.easy_ocr_helper as eoh
import rotate_ocr.ocr_helper.paddle_ocr_helper as poh
import rotate_ocr.ocr_helper.pytesseract_helper as toh
# import yomitoku_helper as yoh
import pprint

print()
print("=======================================")

rotate_img.rotate_img_for_ocr("./test/img_data/test.png", "output")

print("=======================================")

t_ocr = toh.pyTesseractHelper()
print("---------------------------------------")
result = t_ocr.ocr("./test/img_data/test_data.png")
print("---------------------------------------")
pprint.pp(result)

print("=======================================")

p_ocr = poh.PaddleOcrHelper()
print("---------------------------------------")
result = p_ocr.ocr("./test/img_data/test_data.png")
print("---------------------------------------")
pprint.pp(result)

print("=======================================")

e_ocr = eoh.EasyOcrHelper()
print("---------------------------------------")
result = e_ocr.ocr("./test/img_data/test_data.png")
print("---------------------------------------")
pprint.pp(result)

print("=======================================")

# y_ocr = yoh.YomiTokuHelper()
# print("---------------------------------------")
# result = y_ocr.ocr("./test/img_data/test_data.png")
# print("---------------------------------------")
# pprint.pp(result)

# print("=======================================")
