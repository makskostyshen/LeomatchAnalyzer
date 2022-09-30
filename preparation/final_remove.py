

def prepare(df_origin):
    df = df_origin.copy()

    df.drop(["u_date_time", "p_date_time"], axis=1, inplace=True)
    df.drop(["media1", "media2", "media3"], axis=1, inplace=True)
    return df
