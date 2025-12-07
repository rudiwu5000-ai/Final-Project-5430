import praw
import pandas as pd

# Same as the reddit scrape, the actual credentail is not included
CLIENT_ID = ""
CLIENT_SECRET = ""
USER_AGENT = "wsb_top_posts_title_scraper_v1.1 by /u/REDDIT_USERNAME" 

SUBREDDIT_NAME = "wallstreetbets"
LIMIT_COUNT = 3000
OUTPUT_FILENAME = "wsb3000.csv"

def scrape_top_posts_titles():
    """
    Scrapes the top 1000 posts of all time from r/wallstreetbets and outputs 
    only the Index and Title columns.
    """
    
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )
        if not CLIENT_ID or not CLIENT_SECRET:
            print("Error")
        
    except Exception as e:
        print(f"Failed to initialize PRAW: {e}")
        return

    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    posts_data = []
    

    for post in subreddit.top(time_filter="all", limit=LIMIT_COUNT):
        posts_data.append({
            'Title': post.title
        })

    if posts_data:
        df = pd.DataFrame(posts_data)
        df.insert(0, 'Index', range(1, 1 + len(df)))
        df = df[['Index', 'Title']]
        
        df.to_csv(OUTPUT_FILENAME, index=False)
        print("Successfull")
    else:
        print("No posts")

if __name__ == "__main__":
    scrape_top_posts_titles()