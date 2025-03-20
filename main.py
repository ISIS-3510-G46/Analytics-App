from analysis import analyze_posts
from database import fetch_posts






def main():
    posts = fetch_posts()
    if posts:
        df = analyze_posts(posts)
        df.to_csv("transformed_posts_data.csv", index=False)


main()