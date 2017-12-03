import typing as t
from . import config
from time import sleep
from urllib.parse import urljoin
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(config.CK, config.CS, config.AT, config.ATS)

def all_likes(sleep_time: int = 0, max_id: str = None, count: int = 20, path: str = 'favorites/list.json') -> t.Generator[dict, None, None]:
    api_url = urljoin(config.API_BASE, path)
    while True:
        params = { 'max_id': max_id, 'count': count }
        res = twitter.get(api_url, params=params)
        likes = res.json()
        if res.ok and len(likes) != 0:
            yield from likes
            max_id = likes[-1]['id']
            sleep(sleep_time)
        elif len(likes) != 0:
            break
        else:
            raise RuntimeError("Twitter API didn't responds with 2xx: {}".format(res.reason))
