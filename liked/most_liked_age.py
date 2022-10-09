import most_liked_value

column_name = "age"
threshold = 10

def get(df):
    return most_liked_value.get_most_liked_value(df, column_name, threshold)
