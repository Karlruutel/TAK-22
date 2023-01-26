import praw

reddit = praw.reddit(
    client_id = ""
    client_secet = ""
    user_agent = ""
)

print(reddit.read_only)

for submission in reddit.subreddit("eesti").hot(limit=10)
    print(submission.title)