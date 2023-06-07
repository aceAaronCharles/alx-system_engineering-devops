#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively retrieves the titles of all hot articles in a given subreddit,
    counts the occurrences of given keywords, and prints the results.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences for.
        after (str): The 'after' parameter for pagination (default: None).
        word_count (dict): A dictionary to store the count of each keyword (default: None).

    Returns:
        None
    """
    if word_count is None:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {"after": after} if after else None

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            words = title.split()

            for word in words:
                word = word.lower()
                if word in word_list:
                    word_count[word] = word_count.get(word, 0) + 1

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_count:
                print(f"{word}: {count}")
    else:
        return None
