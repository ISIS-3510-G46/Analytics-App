import pandas as pd

def analyze_posts(posts):
    df = pd.DataFrame(posts)

    # Convert price (COP) to numeric (remove commas and convert to integer)
    df["price"] = df["price"].str.replace(",", "").astype(int)
    print(df)
    return df



