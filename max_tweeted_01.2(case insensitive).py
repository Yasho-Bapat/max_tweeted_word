# in this we're testing how the bot will filter words and which words to filter, and have made it case insensitive
# THIS VERSION WORKS WITH AND TESTS OUT FILTERING
# this version uses 2 index-matched lists, the dictionary version will be written later
# 29-10-2021
# this version pulls all tweets of the user up to 3,385 tweets (i think)
#       did pull mine and aarya's 2,900 and 3,100 tweets but not shriya's 11.1k tweets
# case insensitive done: benefits - shorter word list, hopefully more efficient and optimized
# next version: figure out how to pull user ID from follower list instead of manual input

import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

words_list = []  #initializing 3 main important lists
words_count_list = []
words_to_filter = []

filtering = open('words_to_filter.txt')   #making the filtering list
for line in filtering:
    words_to_filter = line.split()

all_tweets = []     #from this line to line 40 is getting ALL tweets by user. without this max tweet count is 200
user = input("enter user: ")
statuses_count = api.get_user(user).statuses_count
print(statuses_count)

target_timeline = api.user_timeline(screen_name = user, count = 200)
all_tweets.extend(target_timeline)
oldest_id = all_tweets[-1].id - 1

while len(target_timeline) > 0:
    target_timeline = api.user_timeline(screen_name = user, count = 50, max_id = oldest_id,)
    all_tweets.extend(target_timeline)
    oldest_id = all_tweets[-1].id - 1

target_timeline =  api.user_timeline(screen_name = user, count = statuses_count - len(all_tweets))
all_tweets.extend(target_timeline)

print(len(all_tweets))

for tweet in all_tweets:        #main block of code which scans and counts words
    content = (tweet.text).split()
    for word in content:
        word = str(word).lower()  #converting all words to smallcase for easy parsing and correctness -- to overcome issues like YES, Yes and yes all being considered to be different words
        if word not in words_list:
            if word not in words_to_filter:     #filtering
                if word[0] != '@':
                    words_list.append(word)
                    words_count_list.append(int(1))
            else:
                continue
        else:
            index = words_list.index(word)
            words_count_list[index] += 1        #counting


words_count_list_reversed = sorted(words_count_list, reverse=True) #sorting to find maximum count
most_tweeted_index = words_count_list.index(words_count_list_reversed[0])  #finding max value's index and finding the corresponding word
most_tweeted = words_list[most_tweeted_index]

print(words_list)
print(len(words_list))
print(words_to_filter)
print(words_count_list)
print(words_count_list_reversed)
print(most_tweeted_index)
print()
print(user + "'s most tweeted word is " + most_tweeted)
print()
print(words_count_list_reversed[0])

#api.update_status(status = ("@" + user + " 's most tweeted word is " + most_tweeted + " (" + str(words_count_list_reversed[0]) + ")"))