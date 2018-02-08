#!/usr/bin/python

import tweepy
import numpy as np
import pandas as pd
import json
import codecs
import collections
import re

direct="vir_result"
alluser_ids=[]
for i in range(7):
    fname="all0"+str(1+i)
    data_array=[]
    file1="LAB/"+direct+"/user_data/"+fname+"_user.csv"
    with codecs.open(file1, "r", "Shift-JIS", "ignore") as f1:
        data_main = pd.read_table(f1, delimiter=",")
    f1.close()
    user_ids=np.array(data_main['user_id'])
    alluser_ids.append(user_ids)

alluser_ids=np.hstack(alluser_ids)
alluser_ids=np.unique(alluser_ids)
r=re.compile('^[0~9]+$')
alluser_ids1=[]
for x in alluser_ids:
    alluser_ids1.append(int(re.findall(r'[0-9]+',x)[0]))

# ログイン設定
twitter_conf1 = {
    'consumer' : {
        'key'    : "NVgv2DuCGCN81DaHmH2PGuKWF",
        'secret' : "4HSnVYomyA5fY1f7YyooW53IAGGBE6aliEloCmJdmBQh8C6djT"
    },
    'access'   : {
        'key'    : "4041533593-Y6lB1BWNXeZpdDk92C2roePZRSJfhVMfF4vunQW",
        'secret' : "4SKVXGEAzNcaQsiLiQ9uH5q1XhB28a0dOxbLbzaqUdx0v"
    }
}
# ログイン設定
twitter_conf2 = {
    'consumer' : {
        'key'    : "isQPIIFrKUkdW81GbghnyKiKv",
        'secret' : "YZwW1RFtpJnKA5ca0adkzDUSqSbycPze7relLpCoDFZ3iJ7WsG"
    },
    'access'   : {
        'key'    : "916137988152688644-Jjwk7S1sMhW05D4aB8ni96DpkxslE6x",
        'secret' : "ioc7uRcANjPDIfnY1OUkkJXnA1xwPq4XEkZvnMWMXlLyh"
    }
}
# ログイン設定
twitter_conf3 = {
    'consumer' : {
        'key'    : "zaJdeNFphQzcev4HKD1Yfa7pV",
        'secret' : "6vYWmP8KsisZaGhWcyG1kkc7pKkbdscRY5IHMCSly4woo4wyx3"
    },
    'access'   : {
        'key'    : "920971157636988929-RbvNltuLQeqGyezchFD9PH6VaMRfEdQ",
        'secret' : "qvGA6RoLKEsUgnqZNlfHG5ss6xGqRz9YvsKscHjPvUEBj"
    }
}
twitter_conf=[twitter_conf1,twitter_conf2,twitter_conf3]
from_num=0
num=0
for ir in range(3):
    for jr in range(100):
        # 認証
        auth = tweepy.OAuthHandler(
            twitter_conf[ir]['consumer']['key'],
            twitter_conf[ir]['consumer']['secret'])
        auth.set_access_token(
            twitter_conf[ir]['access']['key'],
            twitter_conf[ir]['access']['secret'])
        # tweepy初期化
        api = tweepy.API(auth)

        userid = int(alluser_ids1[num+from_num])
        num=num+1
        #numberOfTweets=3100
        #max_id=952425392882647040

        friends_ids = []
        follow_names=[]

        for friend_id in tweepy.Cursor(api.friends_ids, user_id=userid).items():
            friends_ids.append(friend_id)

        for i in range(0, len(friends_ids),100):
            for user in api.lookup_users(user_ids=friends_ids[i:i+100]):
                follow_names.append(user.screen_name)

        follow_all=[]
        follow_all=np.array(follow_names)
        follow_all = pd.DataFrame(follow_all)
        follow_all.to_csv("LAB/usa_election/result_vir_per/user_timeline/follow"+str(userid)+".csv",encoding="SHIFT-JIS")

        remain = True #ループ判定
        userTweets=[]
        cont=0
        while remain:
            cont=cont+1
            new_tweet = api.user_timeline(user_id = userid, count=200)
            for tweet in new_tweet:
                ktweet=json.dumps(tweet._json)
                ktweet=json.loads(ktweet)
                with open('LAB/usa_election/result_vir_per/user_timeline/'+str(userid)+'.txt','a') as tr:
                        tr.write(str(ktweet['text'])+' ')

            if cont > 16:
                remain = False