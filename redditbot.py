#!/usr/bin/python
import praw
import pdb
import re
import os




reddit = praw.Reddit('bot1')




# create an empty list
if not os.path.isfile("Posts_Replied.txt"):
    Posts_Replied = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("Posts_Replied.txt", "r") as f:
        Posts_Replied = f.read()
        Posts_Replied = Posts_Replied.split("\n")
        Posts_Replied = list(filter(None, Posts_Replied))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    print(submission.title)
    # If we haven't replied to this post before
    if submission.id not in Posts_Replied:

       
        if re.search("python test =)", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Hey Master, Good Test!!")
            print("SuperBot says: ", submission.title)

            # Store the current id into our list
            Posts_Replied.append(submission.id)

# Write our updated list back to the file
with open("Posts_Replied.txt", "w") as f:
    for post_id in Posts_Replied:
         f.write(post_id + "\n")






        


