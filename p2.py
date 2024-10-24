from annotat import annotation
from parser import val_input
from images import download_images
from ImageIterator import ImageIterator


def main() -> None:
    try:
        args=val_input()
        download_images(args.pic, args.keyw, args.maxn)
        annotation(args.pic, args.annotationf)
        iterator = ImageIterator(args.annotationf)
        for i in iterator:
            print(i)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()


