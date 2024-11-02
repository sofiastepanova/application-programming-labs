import argparse
from hatftone import halftone, image_res, save_halftone
from histogram import draw, histogram
from load import h_w, l_image


def pars()->tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_image", type=str, help="path to default image")
    parser.add_argument("output_image", type=str, help="path to the new image")
    args = parser.parse_args()
    return args.input_image, args.output_image


def main():
    try:
        im, oim=pars()
        image=l_image(im)
        width, height= h_w(image)
        print(f"Размер изображения: {width}x{height} ")
        r, g, b = histogram(image)
        draw(r, g, b)
        gray_image=halftone(image)
        image_res(image, gray_image)
        save_halftone(gray_image, oim)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()













