
#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list of titles for all hot articles in a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves the titles of all hot articles in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of hot article titles (default: []).
        after (str): The 'after' parameter for pagination (default: None).

    Returns:
        list: A list containing the titles of all hot articles in the subreddit,
              or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": 'Aaron0Chillz'}
    params = {"after": after} if after else None

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
