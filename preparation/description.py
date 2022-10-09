def replace_empty(df_origin):
    df = df_origin.copy()
    df["description"] = df["description"].fillna("")
    return df
