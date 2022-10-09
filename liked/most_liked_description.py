import most_liked_value

threshold = 10
count_column_name = "words_count"
description_column_name = "description"

def __get_words_count(data_row):
    return len(data_row[description_column_name].split())


def get_words_counts(df):
    length = df.shape[0]

    words_counts = []

    for i in range(length):
        row = df.iloc[i]
        words_counts.append(__get_words_count(row));

    return words_counts


def get(df):
    df_description = df.copy()
    df_description[count_column_name] = get_words_counts(df_description)
    return most_liked_value.get_most_liked_value(df_description, count_column_name, threshold)

