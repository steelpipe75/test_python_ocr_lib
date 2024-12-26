import rotate_ocr.process_image as process_image
import argparse

def proc_ocr(input_path, output_dir_path, mode, output_size_file_path):
    process_image.process_image(input_path, output_dir_path, mode, output_size_file_path)

def cli():
    parser = argparse.ArgumentParser(
                    prog="proc_ocr",
                    description="Process an image"
                )
    parser.add_argument("input_path", help="Path to the input image")
    parser.add_argument("output_dir_path", help="Path to the output image & ocr text")
    parser.add_argument("mode", help="OCR mode (t: Tesseract, e: Easy OCR, p: Paddle OCR) e.g. tep")
    parser.add_argument("output_size_file_path", help="Path to the output size file")
    args = parser.parse_args()
    proc_ocr(args.input_path, args.output_dir_path, args.mode, args.output_size_file_path)

if __name__ == "__main__":
    cli()
