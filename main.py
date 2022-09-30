import pandas as pd

from tabulate import tabulate
from preparation.prepare import prepare
import reader

# import crutch

df = reader.read()

df = prepare(df)



print(tabulate(df.head(10), headers="keys"))