import boto3
import pandas as pd
import tweepy
import time
from datetime import datetime

# Twitter config
BEARER_TOKEN = "Your bearer token" #login to twitter dvelopment create app get your bear token
USER_ID = 44196397  # Elon Musk's user ID


# Initialize Twitter client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets(user_id, max_results=100):
    try:
        response = client.get_users_tweets(
            id=user_id,
            max_results=max_results,
            tweet_fields=["created_at", "lang", "text"]
        )
        return response.data
    except tweepy.TooManyRequests as e:
        reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 900))
        wait_seconds = max(reset_time - time.time(), 60)
        print(f"[Rate Limit] Sleeping for {int(wait_seconds)} seconds before retrying...")
        time.sleep(wait_seconds)
        return fetch_tweets(user_id, max_results)

def main():
    print(f"[{datetime.utcnow()}] Fetching tweets for user ID {USER_ID}...")
    tweets = fetch_tweets(USER_ID)

    if not tweets:
        print("No tweets found.")
        return

    tweets_data = []
    for tweet in tweets:
        tweets_data.append({
            "id": tweet.id,
            "created_at": tweet.created_at.isoformat(),
            "text": tweet.text,
            "lang": tweet.lang
        })

    df = pd.DataFrame(tweets_data)

    # Save locally (optional)
    local_file = 'elonmusk_tweets.csv'
    df.to_csv(local_file, index=False)
    print(f"Saved tweets locally to {local_file}")


if __name__ == "__main__":
    main()
