# in this we're testing how the bot will filter words and which words to filter
# THIS VERSION WORKS WITH AND TESTS OUT FILTERING
# this version uses 2 index-matched lists, the dictionary version will be written later
# 27-10-2021
# find a way to cycle through all tweets -- can pull only 200 at a time in future version
# make case insensitive in next version

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

user = input("Enter user: ")
target_timeline = api.user_timeline(screen_name = user, count = 200, include_rts = False)

for tweet in target_timeline:
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
print(words_to_filter)
print(words_count_list)
print(words_count_list_reversed)
print(most_tweeted_index)
print()
print(user + "'s most tweeted word is " + most_tweeted)
print()
print(words_count_list_reversed[0])