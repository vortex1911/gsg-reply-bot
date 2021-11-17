import praw
import re

r = praw.Reddit('bot-gsg-bot')
subreddit = r.subreddit("gaming")

f = open('comments-responded-to.txt', 'a')
f = open('comments-responded-to.txt', 'r+')
IDs = f.readlines()

while True:
    for submission in subreddit.hot(limit=2):
        print("Title: ", submission.title)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            if str(comment.id) + '\n' not in IDs:
                if re.search("Grove Street Games", comment.body, re.IGNORECASE) or re.search("GroveStreetGames",
                                                                                             comment.body,
                                                                                             re.IGNORECASE):
                    print(comment.body)
                    comment.reply("Correction. Its actually Grocery Street Games. Have a nice day.")
                    print("Writing to file id:" + comment.id)
                    f.write(comment.id + '\n')
    f.close()
