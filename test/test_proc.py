import rotate_ocr.process_image as process_image


def test_process_image():
    process_image.process_image(
            "./test/img_data/test_data.png",
            "./output",
            "rp",
            "./output/output_size.csv",
        )

if __name__ == "__main__":
    test_process_image()
