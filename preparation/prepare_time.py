import pandas as pd

def prepare(df_origin):
    df = df_origin.copy()

    # read datetime as datetime
    df["u_date_time"] = pd.to_datetime(df["u_date_time"])
    df["p_date_time"] = pd.to_datetime(df["p_date_time"])


    # divide time from date
    df.insert(0, "u_date", df["u_date_time"].dt.date)
    df.insert(1, "u_time", df["u_date_time"].dt.time)

    df.insert(4, "b_date", df["p_date_time"].dt.date)
    df.insert(5, "b_time", df["p_date_time"].dt.time)

    return df
