# in this we're testing how the bot will filter words and which words to filter
# THIS VERSION WORKS WITH AND TESTS OUT FILTERING
# this version uses 2 index-matched lists, the dictionary version will be written later
# 28-10-2021
# this version pulls all tweets of the user up to 4,000 tweets (i think)
#       did pull mine and aarya's 2,900 and 3,100 tweets but not shriya's 11.1k tweets
# make case insensitive in next version, figure out why elon's tweets cannot be fully pulled

import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

words_list = []
words_count_list = []
words_to_filter = []

filtering = open('words_to_filter.txt')
for line in filtering:
    words_to_filter = line.split()

all_tweets = []
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


target_timeline =  api.user_timeline(screen_name = user, count = len(all_tweets) - statuses_count)
all_tweets.extend(target_timeline)

print(len(all_tweets))

for tweet in all_tweets:
    content = (tweet.text).split()
    for word in content:
        if word not in words_list:
            if word not in words_to_filter:
                if word[0] != '@':
                    words_list.append(word)
                    words_count_list.append(int(1))
            else:
                continue
        else:
            index = words_list.index(word)
            words_count_list[index] += 1


words_count_list_reversed = sorted(words_count_list, reverse=True)
most_tweeted_index = words_count_list.index(words_count_list_reversed[0])
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