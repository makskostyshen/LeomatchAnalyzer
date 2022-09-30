from preparation import prepare_media
from preparation import add_time_differences
from preparation import final_remove
from preparation import prepare_time


def prepare(df_origin):

    df = df_origin.copy()

    df = prepare_time.prepare(df)

    # add time difference info
    time_diff_info = add_time_differences.add(df)
    df["who_first"] = time_diff_info[0];
    df["time_diff"] = time_diff_info[1];


    # add types and count
    media_count, media_types = prepare_media.get_media_info(df)

    df["media_types"] = media_types
    df["media_count"] = media_count


    # replace empty profile answers with DISLIKE
    df["p_type"] = df["p_type"].fillna("DISLIKE")


    # replace empty names
    df["name"] = df["name"].fillna("")


    # remove
    df = final_remove.prepare(df)

    return df

