def replace(df_origin):
    df = df_origin.copy()

    df["p_type"] = df["p_type"].fillna("DISLIKE")

    df["name"] = df["name"].fillna("")

    return df