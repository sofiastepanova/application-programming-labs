import cv2
import matplotlib.pyplot as plt
import pandas as pd


def cr_df(annotation_file: str) -> pd.DataFrame:
    """
    создание DataFrame
    :param annotation_file: путь к annotation file
    :return: DataFrame
    """
    df = pd.read_csv(annotation_file)
    df.columns=['Abspath', 'Relpath']
    return df


def h_w_d(df: pd.DataFrame) -> None:
    """
    добавление столбцов: height, width, depth
    :param df: Original DataFrame
    :return: None
    """
    h = []
    w = []
    d = []
    for i in df["Relpath"]:
        sizes = cv2.imread(i).shape
        h.append(sizes[0])
        w.append(sizes[1])
        d.append(sizes[2])

    df.insert(2, "Height", pd.Series(h), True)
    df.insert(3, "Width", pd.Series(w), True)
    df.insert(4, "Depth", pd.Series(d), True)


def statistical(df: pd.DataFrame) -> pd.DataFrame:
    """
    создание статистики
    :param df: DataFrame со статистикой
    :return: Статистическая информация о столбцах: "Height", "Width", "Depth"
    """
    return df.loc[:, ("Height", "Width", "Depth")].describe()


def filter_df(df: pd.DataFrame, max_height: float, max_width: float) -> pd.DataFrame:
    """
    Фильтрация DataFrame по максимальной высоте и ширине
    :param df: Исходный DataFrame
    :param max_height: макс высота
    :param max_width: макс ширина
    :return: отфильтрованный DataFrame
    """
    return df[(df["Height"] < max_height) & (df["Width"] < max_width)]


def add_area(df: pd.DataFrame) -> None:
    """
    добавить столбцы
    :param df: исходный DataFrame
    :return: None
    """
    df["Area"] = df["Height"]*df["Width"]


def filter_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    фильтрация DataFrame по площ
    :param df: исходный DataFrame
    :return: отфильтрованный DataFrame
    """
    return df.sort_values(by="Area")


def hist(df: pd.DataFrame) -> None:
    """
    создание гистограммы
    :param df: DataFrame
    :return: None
    """
    df["Area"].plot()
    plt.title('Histogram of areas')
    plt.xlabel('Image')
    plt.ylabel('Area')
    plt.show()
