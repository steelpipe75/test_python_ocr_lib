import rotate_ocr.process_image as process_image
import argparse

def proc_ocr(input_path, output_path):
    process_image.process_image(input_path, output_path)

def __cmd():
    parser = argparse.ArgumentParser(
                    prog="proc_ocr",
                    description="Process an image"
                )
    parser.add_argument("input_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to the output image & ocr text")
    args = parser.parse_args()
    proc_ocr(args.input_path, args.output_path)

if __name__ == "__main__":
    __cmd()
