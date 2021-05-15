import threading
import time
import tweepy
from bot import *


class tweetThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Start " + self.name + " thread")
        api = tweepy.API(auth)
        LIST_ID = "1393384898971439105"
        print("Successfully connection to @" + str(api.me().screen_name))
        user_List = api.get_list(list_id=LIST_ID)
        print("Found list: " + user_List.name)
        for member in api.list_members(list_id=LIST_ID):
            print("Found a member: " + member.screen_name)
        print("Load list total members: " + str(user_List.member_count))
        while True:
            print("Search tweets")
            for status in tweepy.Cursor(api.search, q="time.is/EST").items():
                try:
                    print("xd")
                except tweepy.TweepError as ex:
                    print(ex.reason)
            time.sleep(120)  # 2 minutes
