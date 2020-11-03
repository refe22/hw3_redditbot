from textblob import TextBlob
import praw
import random
import datetime

reddit_threads = []
reddit = praw.Reddit('lbot')


reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jn3fjq/mitch_mcconnell_just_adjourned_the_senate_until/'
submission = reddit.submission(url=reddit_debate_url)
submission.comments.replace_more(limit=None)
"""
for thread in reddit.subreddit('csci040temp').top(time_filter='all'):
    reddit_threads.append(thread)
    thread_new = random.choice(reddit_threads)
    submission = reddit.submission(id=thread_new)
"""
#extra credit 1
for comment in submission.comments.list():
    if 'trump'in comment.body.lower():
        comment.upvote()
        print('upvoted')

#extra credit 2
for comment in submission.comments.list():
    #print(comment)
    target_submission = TextBlob(str(comment.body))
    #print(target_submission)
    polarity = target_submission.sentiment.polarity
    #print(polarity)
    if 'trump' in comment.body.lower() and polarity > 0:
        comment.upvote()
        print('Upvote')

    if 'biden' in comment.body.lower() and polarity > 0:
        comment.downvote()
        print('Downvote')
    if 'biden' in comment.body.lower() and polarity < 0:
        comment.upvote()
        print('upvote')
    if 'trump' in comment.body.lower() and polarity < 0:
        comment.downvote()
        print('downvote')    

