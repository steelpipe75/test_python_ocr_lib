import rotate_ocr.process_image as process_image
import argparse

def proc_ocr(input_path, output_path, mode):
    process_image.process_image(input_path, output_path, mode)

def cli():
    parser = argparse.ArgumentParser(
                    prog="proc_ocr",
                    description="Process an image"
                )
    parser.add_argument("input_path", help="Path to the input image")
    parser.add_argument("output_dir_path", help="Path to the output image & ocr text")
    parser.add_argument("mode", help="OCR mode (t: Tesseract, e: Easy OCR, p: Paddle OCR) e.g. tep")
    args = parser.parse_args()
    proc_ocr(args.input_path, args.output_dir_path, args.mode)

if __name__ == "__main__":
    cli()
