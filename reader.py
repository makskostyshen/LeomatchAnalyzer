import pandas as pd

path = 'C:\\Users\\maxxx\\Desktop\\DaiVinchikProject\\maks_kostyshen\\profiles.csv'


def __read_time(df_origin):
    df = df_origin.copy()

    df["u_date_time"] = pd.to_datetime(df["u_date_time"])
    df["p_date_time"] = pd.to_datetime(df["p_date_time"])

    return df


def __correct_columns(df_origin):
    df = df_origin.copy()

    df = df[["userInteractionTime", "userInteractionType",
             "profileInteractionTime", "profileInteractionType",
             "name", "age", "city", "description", "media1", "media2", "media3"]]

    df = df.rename(columns={
        "userInteractionTime": "u_date_time",
        "profileInteractionTime": "p_date_time",
        "userInteractionType": "u_type",
        "profileInteractionType": "p_type"})

    return df


def __filter_incorrect(df_origin):
    df = df_origin.copy()

    df = df.dropna(subset=["media1"])
    return df


def read():
    df = pd.read_csv(path, index_col="id")

    df = __correct_columns(df)

    df = __filter_incorrect(df)

    df = __read_time(df)

    return df











