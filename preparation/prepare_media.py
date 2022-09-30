def get_media_count(data_row):
    if type(data_row["media2"]) == float:
        return 1
    elif type(data_row["media3"]) == float:
        return 2
    else:
        return 3


def get_media_type(data_row):
    if "photos" in data_row["media1"]:
        return "photo"
    else:
        return "video"


def get_media_info(df):
    length = df.shape[0]

    media_types = []
    media_count = []

    for i in range(length):
        row = df.iloc[i]
        media_types.append(get_media_type(row));
        media_count.append(get_media_count(row));

    return media_count, media_types
