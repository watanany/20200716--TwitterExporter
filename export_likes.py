import sys
from twitter_exporter import all_likes

GET_TWEET_URL = 'https://twitter.com/{}/status/{}'

def main() -> None:
    for like in all_likes(sleep_time=20, max_id='358878880335011840'):
        tweet_url = GET_TWEET_URL.format(like['user']['screen_name'], like['id'])
        print(tweet_url)
        sys.stdout.flush()

if __name__ == '__main__':
    main()
