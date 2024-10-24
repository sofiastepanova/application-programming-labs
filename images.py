import os
from icrawler.builtin import GoogleImageCrawler
import shutil


def download_images(pic: str, keyw: str, maxn: int) -> None:
    """
    Функция загружает изображения с помощью BingImageCrawler
    :param pic:директория с изображениями
    :param keyw:ключевое слово
    :param maxn:кол-во изображений
    :return: none
    """
    if os.path.exists(pic):
        shutil.rmtree(pic)
        os.mkdir(pic)
    else:
        os.mkdir(pic)

    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage = {'root_dir': 'pic'})
    filters = dict(
        size='large',
        color='gray')
    google_crawler.crawl(keyword=keyw, filters=filters, max_num=maxn)