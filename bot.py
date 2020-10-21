import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment functions from the week_07 lab here
"""
def generate_comment_0():
    names = ['Trump', 'President Trump', 'Donald Trump', 'Donald']
    name = random.choice(names)
    diseases =['COVID-19', 'Corona', 'the virus', 'pandemic']
    disease = random.choice(diseases)
    voting=['vote', 'cast my ballot', 'consider voting', 'think about voting']
    votes =random.choice(voting)
    locations = ['isolation', 'lockdown', 'quarantine', 'local store closings']
    location = random.choice(locations)
    importance = ['serious', 'important', 'a concern', 'a serious problem']
    important = random.choice(importance)
    text = 'I will '+votes+' for '+ name +' because he knows that '+ disease+' is '+important+' but so is the fact that there are suffering communities due to the '+location+'. That is '+important+' too.'
    return text
#print('text=',generate_comment_0())

def generate_comment_1():
    parties=['Red', 'for the Republican Party candidate', 'conservative', 'for a Republican Administration']
    party = random.choice(parties)
    greetings = ['Hey', 'Hello', 'Hi', 'Howdy']
    greeting = random.choice(greetings)
    judges = ['judges', 'make good judge appointments', 'important appointments', 'strong appointments']
    judge = random.choice(judges)
    importance = ['important', 'great', 'needed', 'powerful']
    important = random.choice(importance)
    jobs =['decisions', 'changes', 'freedoms', 'rulings']
    job =random.choice(jobs)
    text = greeting+' voter. I will vote '+party+' and you should too to support new '+judge+' to Federal Courts. They will help create '+important+' '+job+' in the future.' 
    return text
#print('text=',generate_comment_1())

def generate_comment_2():
    actions = ['support', 'vote for', 'encourage people to vote for', 'be voting for']
    action = random.choice(actions)
    names = ['Trump', 'President Trump', 'Donald Trump', 'Donald']
    name = random.choice(names)
    times = ['election', 'fall', '2020 election', 'election season']
    time = random.choice(times)
    qualities=['have a great personal life', 'be a perfect person', 'be the best character', 'be inspirational']
    quality=random.choice(qualities)
    beginnings =['Even though', 'Despite the fact', 'In spite of the fact', 'Although']
    beginning = random.choice(beginnings)
    text = beginning+' he may not '+quality+', I will '+action+' '+name+ ' this '+time+'. This is because when it comes to policy, '+name+' has a good track record.'
    return text
#print('text=',generate_comment_2())

def generate_comment_3():
    names = ['Biden', 'Vice President Biden', 'Joe Biden', 'Joe']
    name = random.choice(names)
    actions = ['plans to do', 'wants to do', 'hopes to do', 'intends to do']
    action = random.choice(actions)
    voting = ['vote for', 'support', 'cast your ballot for', 'elect']
    vote = random.choice(voting)
    steps=['progress', 'improve', 'advance', 'make strides forward']
    step = random.choice(steps)
    qualities=['seem', 'appear', 'sound', 'be deemed as']
    quality=random.choice(qualities)
    locations= ["this country", "America", "the United States", "the US"]
    location = random.choice(locations)
    text = "Don't "+vote+" " +name+ " because what he "+action+' will not help us '+step+'. His ideas might '+quality+' proactive but they will not restore '+location+"."
    return text
#print('text=',generate_comment_3())

def generate_comment_4():
    names = ['Biden', 'Vice President Biden', 'Joe Biden', 'Joe']
    name = random.choice(names)
    names2 = ['Biden', 'Vice President Biden', 'Joe Biden', 'Joe']
    name2 = random.choice(names2)
    persons = ['Trump', 'President Trump', 'Donald Trump', 'Donald']
    person = random.choice(persons)
    categories =['economy', 'racial tensions', 'small businesses', 'state of the union']
    category = random.choice(categories)
    locations= ["this country's", "America's", "the United States'", "the US'"]
    location = random.choice(locations)
    reasons = ['just because', 'because', 'only due to the fact that', 'only on the fact that']
    reason = random.choice(reasons)
    text = "No one should just vote for "+name+ " "+reason+" he isn't "+person+". "+name2+" doesn't have a good plan for "+location+" "+category+" right now." 
    return text
#print('text=',generate_comment_4())

def generate_comment_5():
    names = ['Biden', 'Vice President Biden', 'Joe Biden', 'Joe']
    name = random.choice(names)
    names2 = ['Biden', 'Vice President Biden', 'Joe Biden', 'Joe']
    name2 = random.choice(names2)
    categories =['order', 'law and order', 'restoration', 'unity']
    category = random.choice(categories)
    locations= ["this country", "America", "the United States", "the US", "the USA"]
    location = random.choice(locations)
    plans=['plans', 'administration proposals', "party's platform", 'policy plans']
    plan =random.choice(plans)
    text = "Reconsider your vote for "+name+" and check his party's "+plan+". Based on these, "+name2+" will not bring "+category+" to "+location+"."
    return text
#print('text=',generate_comment_5())

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    options = [0,1,2,3,4,5]
    choice =random.choice(options)
    #print(choice)
    if choice == 0:
        print(generate_comment_0())
    if choice == 1:
        print(generate_comment_1())
    if choice == 2:
        print(generate_comment_2())
    if choice == 3:
        print(generate_comment_3())
    if choice == 4:
        print(generate_comment_4())
    if choice == 5:
        print(generate_comment_5())
    text = ''
    return text

for i in range(1000):
    print(generate_comment())

"""
# connect to reddit 
reddit = praw.Reddit('lbot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
#while True:
if True: 

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=1)
    all_comments = []
    for comment in submission.comments.list():
        if comment not in all_comments:
            all_comments +=all_comments.append(comment) 
        else:
            continue
#print(len(all_comments))
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
print('len(all_comments)=',len(all_comments))

"""
    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
not_my_comments = []

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if not has_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
"""
