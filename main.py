from analysis import analyze_posts, analyze_favorites
from database import fetch_posts, fetch_favorites






def main():
    posts = fetch_posts()
    favorites, favorite_events = fetch_favorites()
    if posts:
        df = analyze_posts(posts)
        df.to_csv("transformed_posts_data.csv", index=False)
    
    if favorites:
        df, df_events = analyze_favorites(favorites, favorite_events)
        df.to_csv("favorites_data.csv", index=False)
        df_events.to_csv("favorite_events.csv")
    



main()