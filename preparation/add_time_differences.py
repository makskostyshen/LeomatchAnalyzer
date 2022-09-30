import numpy as np
import pandas as pd


def __get_time_diff_row(row):
    u_date_time = row["u_date_time"]
    p_date_time = row["p_date_time"]

    if pd.isnull(p_date_time):
        return "user", np.nan

    time_diff_object = u_date_time - p_date_time;

    if time_diff_object.days >= 0:
        who_first = "user"
        time_diff = time_diff_object.seconds
    else:
        who_first = "bot"
        time_diff = (p_date_time - u_date_time).seconds

    return who_first, time_diff


def add(df):
    length = df.shape[0]

    who_first = []
    time_diff = []

    for i in range(length):
        row = df.iloc[i]
        time_info = __get_time_diff_row(row)
        who_first.append(time_info[0]);
        time_diff.append(time_info[1]);

    return who_first, time_diff
