import pandas as pd
import numpy as np

def __get_time_diff_row(row):
    u_date_time = row["u_date_time"]
    p_date_time = row["p_date_time"]

    if pd.isnull(p_date_time):
        return "user", np.nan

    time_diff_object = u_date_time - p_date_time

    if time_diff_object.days >= 0:
        who_first = "user"
        time_diff = time_diff_object.seconds
    else:
        who_first = "bot"
        time_diff = (p_date_time - u_date_time).seconds

    return who_first, time_diff


def __get_time_diffs(df):
    length = df.shape[0]

    who_first = []
    time_diff = []

    for i in range(length):
        row = df.iloc[i]
        time_info = __get_time_diff_row(row)
        who_first.append(time_info[0]);
        time_diff.append(time_info[1]);

    return who_first, time_diff


def __divide_time(df_origin):
    df = df_origin.copy()

    df.insert(0, "u_date", df["u_date_time"].dt.date)
    df.insert(1, "u_time", df["u_date_time"].dt.time)

    df.insert(4, "b_date", df["p_date_time"].dt.date)
    df.insert(5, "b_time", df["p_date_time"].dt.time)

    return df

def prepare(df_origin):
    df = df_origin.copy()

    df = __divide_time(df)

    time_diffs_info = __get_time_diffs(df)
    df["who_first"] = time_diffs_info[0];
    df["time_diff"] = time_diffs_info[1];

    return df
