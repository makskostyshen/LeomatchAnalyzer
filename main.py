import pandas as pd

from tabulate import tabulate
from preparation.prepare import prepare

from liked import most_liked_name
from liked import most_liked_city
from liked import most_liked_media_count
from liked import most_liked_media_types
from liked import most_liked_age
from liked import most_liked_description
import reader


df = reader.read()

df = prepare(df)


most_liked_name_series = most_liked_name.get(df)
print(most_liked_name_series)

print("=====")

most_liked_city_series = most_liked_city.get(df)
print(most_liked_city_series)

print("=====")

most_liked_media_count_series = most_liked_media_count.get(df)
print(most_liked_media_count_series)

print("=====")

most_liked_media_types_series = most_liked_media_types.get(df)
print(most_liked_media_types_series)

print("=====")

most_liked_age_series = most_liked_age.get(df)
print(most_liked_age_series)

print("=====")

most_liked_description = most_liked_description.get(df)
print(most_liked_description)

print("=====")

print(tabulate(df.head(10), headers="keys"))


