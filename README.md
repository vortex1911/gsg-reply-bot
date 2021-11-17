# gsg-reply-bot
A simple reddit bot to respond "Correction. Its actually Grocery Street Games. Have a nice day." whenever someone comments "Grove Street Games" in the subreddit r/Gaming.

# Setup
Install praw and MLB-StatsAPI:

`pip install praw pip`

Run gsg-reply-bot\main.py in Python and either pass the subreddit(s) as a parameter or enter when prompted.

`py -3 gsg-reply-bot\main.py`

### Make sure your praw.ini has the following entries

[bot-gsg-bot] //This id will be used as identifier to load the config onto the code

client_id=

client_secret=

password=

username=

user_agent=


