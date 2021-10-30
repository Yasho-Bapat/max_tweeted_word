# max_tweeted_word
This code is for a bot which will find a Twitter user's most tweeted word and tweet that word, tagging said user

The program uses tweepy to access Twitter API

_HOW THE BOT WORKS:_
The bot will scan through its followers and for every follower, will scan the user's tweets and tweet their most tweeted word in the format: @username's most tweeted word is [word] (*number of times word is used*)

To find their most tweeted word, a Twitter user will have to follow this bot's account.

As of now, a user following the bot will not act as a trigger. I will manually be running the bot from my machine a few times a day to work it.

LOGIC
1) Getting a user from followers list:
  - first, I open a blank .txt file
  - next, using the api.followers(user) function, I pulled the bot's followers
  - scan through the followers and filter out the protected accounts -- add the selected user IDs to a followers_list
  - cycle through the followers_list formed in the above step with a for loop 
  - IF "follower" in the for loop iteration is not in the .txt file, append users_list with "follower" and also append .txt file
  - **the above step makes sure the bot does not run for the same account more than once**
  - choose only 5 users at a time.

2) Finding max tweeted word:
  - This is for chosen user among 5 users in users_list
  - Pull all tweets of the user
    Twitter API limits maximum tweets to be pulled at 200. To bypass this and pull all (up to ~3,500) tweets, cycle through tweets by filtering by using tweet_id which is timestamped
  - store all tweets in a list
  - initialize a words_list and a words_count_list to store the words tweeted by the user and corresponding count
  - in a for loop, for every tweet, pull **tweet.text** to extract the text content mentioned in each element of the tweets list from the step above
  - once tweet.text is extracted, comb through each word with for loop.
    Check if word selected in for loop iteration exists in words_list 
        If YES, then **find index of word in words_list and increment element at index in words_count**
        If NO, check if chosen word in the loop is NOT in the words_to_filter.txt file. If word is not in words_to_filter.txt, append word in words_list and then do index matching as mentioned in the YES step
  - after this, sort the words_count_list in reverse order -- element at pos [0] is the count of the max tweeted word. Find index of element at [0] in sorted list in words_count_list and **the word at this index is the most tweeted word**


3) Tweeting
  - using api.update_status, tweet in the format @username's most  tweeted word is [word] (*number of times word is used*)
