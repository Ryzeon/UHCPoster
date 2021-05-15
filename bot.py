# Created by Ryzeon
# Github: github.ryzeon.me
# Twitter: @Ryzeon_

import tweepy
from botThread import *

auth = tweepy.OAuthHandler("UMOPM", "XDXDX")
auth.set_access_token("XDX-XDXD",
                      "XDXDXD")

def run():
    print("Starting UHCPoster bot!")
    botT = tweetThread("tweets")
    botT.start()


if __name__ == '__main__':
    run()
