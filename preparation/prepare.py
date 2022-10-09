from preparation import media
from preparation import final
from preparation import time
from preparation import description
from preparation import empty


def prepare(df_origin):

    df = df_origin.copy()

    df = time.prepare(df)

    df = description.replace_empty(df)

    df = media.prepare(df)

    df = empty.replace(df)

    df = final.clean(df)

    return df

