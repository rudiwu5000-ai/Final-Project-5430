
import praw
import pandas as pd
from datetime import datetime
import pytz
import time


# Actual client id and secret is not included here since it is tied directly to my personal email and reddit credential.
CLIENT_ID = ""
CLIENT_SECRET = ""
USER_AGENT = "wsb_flair_scraper_v1.0 by /u/REDDIT_USERNAME" 

# Only the flairs of YOLO, Gain, and Loss is scraped
SUBREDDIT_NAME = "wallstreetbets"
TARGET_FLAIRS = ["YOLO", "Gain", "Loss"]
OUTPUT_FILENAME = "wsb_flair_posts_nov_2025.csv"

# Date range: November 1 to November 30

START_TIME_UTC = 1700956800 
END_TIME_UTC = 1701561600 
EST_TZ = pytz.timezone('US/Eastern')

def scrape_wsb_posts():
    """Scrapes posts from r/wallstreetbets with specific flairs and time range."""
    
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )
        if not CLIENT_ID or not CLIENT_SECRET:
            print("Error")
            return
        
    except Exception as e:
        print(f"Failed to initialize PRAW: {e}")
        return

    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    all_posts = []
    flair_query = " OR ".join([f'flair_name:"{flair}"' for flair in TARGET_FLAIRS])



    search_results = subreddit.search(
        query=flair_query,
        sort="new",  
        time_filter="all", 
        limit=None 
    )

    for post in search_results:
        if post.created_utc >= START_TIME_UTC and post.created_utc <= END_TIME_UTC:
            utc_dt = datetime.utcfromtimestamp(post.created_utc).replace(tzinfo=pytz.utc)
            est_dt = utc_dt.astimezone(EST_TZ)
            all_posts.append({
                'Headline': post.title,
                'Timestamp (EST/EDT)': est_dt.strftime('%Y-%m-%d %H:%M:%S %Z'), # Formatted string
                'Flair': post.link_flair_text
            })
            
        elif post.created_utc < START_TIME_UTC:
            print("Reached posts older than the start time")
            break

    # CSV
    if all_posts:
        df = pd.DataFrame(all_posts)
        df.insert(0, 'Index', range(1, 1 + len(df)))
        df = df[['Index', 'Headline', 'Timestamp (EST/EDT)', 'Flair']]
        
        df.to_csv(OUTPUT_FILENAME, index=False)
        print("Successfull")
    else:
        print("No flairs")

if __name__ == "__main__":
    scrape_wsb_posts()