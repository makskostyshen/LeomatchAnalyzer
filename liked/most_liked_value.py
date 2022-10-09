import pandas as pd


def get_most_liked_value(df, column, threshold):
    values_by_name = __get_values_by_name(df, column)

    values_by_likes = __get_values_by_likes(df, column)

    percentage_frame = __get_percentage_frame(values_by_name, values_by_likes)

    percentage_frame = __get_threshold_frame(percentage_frame, threshold)

    return __get_max_value_series(percentage_frame)


def __get_percentage_frame(values_by_name, values_by_likes):
    percentage_frame = pd.concat([values_by_name, values_by_likes], axis=1)
    percentage_frame["times_liked"] = percentage_frame["times_liked"].fillna(0)

    percentage_frame["percentage"] = percentage_frame["times_liked"] / percentage_frame["all_occurrences"]
    return percentage_frame


def __get_max_value_series(percentage_frame):
    index = percentage_frame["percentage"].idxmax()
    return percentage_frame.loc[index]


def __get_values_by_name(df, column):
    values_by_name = df[column].value_counts().to_frame()
    values_by_name = values_by_name.rename(columns={column: "all_occurrences"})
    return values_by_name


def __get_values_by_likes(df, column):
    likes_filter = (df["u_type"] == "LIKE") | (df["u_type"] == "SUPER_LIKE")

    values_by_likes = df.loc[likes_filter, column].value_counts().to_frame()
    values_by_likes = values_by_likes.rename(columns={column: "times_liked"})

    return values_by_likes


def __get_threshold_frame(percentage_frame, threshold):
    threshold_filter = percentage_frame["all_occurrences"] > threshold
    return percentage_frame[threshold_filter]