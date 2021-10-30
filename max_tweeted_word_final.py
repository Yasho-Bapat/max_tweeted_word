# final build
# for users with >4000 tweets, does not pull all tweets due to equipment limitations
# uses 2 index-matched lists -- planning on working on a version using dictionaries
#

import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


users_list = []
followers_list = []
already_scanned = []

followers_doc = open('followers_page.txt')
for line in followers_doc:
    already_scanned = (line.split())

#print(already_scanned)
home_user = bot_username #bot's account's username

for follower in api.followers(screen_name = home_user, count = api.get_user(home_user).followers_count ):
    if not follower.protected:
        followers_list.append(follower.screen_name)

followers_doc_w = open('followers_page.txt', 'a')

for follower in reversed(followers_list):
    if follower not in already_scanned:
        if len(users_list) < 6:
            users_list.append(follower)
            followers_doc_w.write(follower + ' ')
        else:
            continue

words_to_filter = []
filtering = open('words_to_filter.txt')  # making the filtering list
for line in filtering:
    words_to_filter = line.split()

print(users_list)
for user in users_list:

    words_list = []  # initializing 3 main important lists
    words_count_list = []

    print(user)

    all_tweets = []     #from this line to line 40 is getting ALL tweets by user. without this max tweet count is 200
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
                words_count_list[index] += 1        #increment count


    words_count_list_reversed = sorted(words_count_list, reverse=True) #sorting to find maximum count
    most_tweeted_index = words_count_list.index(words_count_list_reversed[0])  #finding max value's index and finding the corresponding word
    most_tweeted = words_list[most_tweeted_index]

    print(user + " 's most tweeted word is " + most_tweeted + " (" + str(words_count_list_reversed[0]) + ")")
    api.update_status(status = ("@" + user + " 's most tweeted word is " + most_tweeted + " (" + str(words_count_list_reversed[0]) + ")"))