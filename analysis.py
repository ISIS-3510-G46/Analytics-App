import pandas as pd

def analyze_posts(posts):
    df = pd.DataFrame(posts)

    # Convert price (COP) to numeric (remove commas and convert to integer)
    df["price"] = df["price"].str.replace(",", "").astype(int)
    print(df)
    return df


def analyze_favorites(favorites, events):
    df = pd.DataFrame(favorites)
    df_events = pd.DataFrame(events)
    df_events['latitude'] = df_events['latitude'].round(4)
    df_events['longitude'] = df_events['longitude'].round(4)
    print(df_events)
    return df, df_events

