import argparse
from p4 import cr_df, h_w_d, statistical, filter_df, add_area, filter_by_area, hist


def get_input() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_csv', type=str, help='name dir')
    args = parser.parse_args()
    path_to_csv = args.path_to_csv
    return path_to_csv


def main() -> None:

    try:
        path_to_csv = get_input()
        df = cr_df(path_to_csv)
        print(df.head())
        h_w_d(df)
        print(df[["Height", "Width", "Depth"]].head())
        print("Statistic:\n", statistical(df))
        print(filter_df(df, 1000, 1000)[["Height", "Width"]].head())
        add_area(df)
        print(filter_by_area(df).head()[["Relpath", "Area"]])
        hist(df)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
