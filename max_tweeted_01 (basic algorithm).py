# in this we're testing how the bot will go through tweets and find the most tweeted word
# there is NO filtering in this version
# this version uses 2 index-matched lists, the dictionary version will be written later
# 26-10-2021

import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

words_list = []
words_count_list = []
user = input("Enter user: ")
target_timeline = api.user_timeline(screen_name = user, count = 1000)

for tweet in target_timeline:
    content = (tweet.text).split()
    for word in content:
        if word not in words_list:
            words_list.append(word)
            words_count_list.append(int(1))
        else:
            index = words_list.index(word)
            words_count_list[index] += 1

words_count_list_reversed = sorted(words_count_list, reverse=True)
most_tweeted_index = words_count_list.index(words_count_list_reversed[0])
most_tweeted = words_list[most_tweeted_index]

print(words_list)
#print(words_count_list)
#print(words_count_list_reversed)
#print(most_tweeted_index)
print(user + "'s most tweeted word is " + most_tweeted)
print(words_count_list_reversed[0])