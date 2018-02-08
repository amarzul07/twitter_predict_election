#!/usr/bin/env python2
# -*- coding: utf-8 -*-

word1="gillespie"
word2="ralph"
word3="northam"
word4="cliff"
word5="hyra"
direct="vir_result"
for i in range(7):
    fname="all0"+str(i+1)
    import json
    import pandas as pd
    import re
    import operator 
    from textblob import TextBlob
    from collections import Counter
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import string
    import os, sys, codecs
    from nltk import bigrams
    import numpy as np

    emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""
     
    regex_str = [
        emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
     
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:\S)' # anything else
    ]
        
    tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
    emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
     
    def tokenize(s):
        return tokens_re.findall(s)
     
    def preprocess(s, lowercase=False):
        tokens = tokenize(s)
        if lowercase:
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via'] 

    tweets = []
    for line in open("/Users/amarzulgantumur/LAB/usa_election/datatxt/"+fname+".txt"):
        line1=json.dumps(line)
        tweets.append(json.loads(line1))
            
    tw_array=[]
    tw_text=[]
    df=[]
    count=1
    for d in tweets:
        each_tw=[]
        data=json.loads(d)
        text=data.get('text')
        if type(text)=='unicode':
            text=text.encode('utf-8')
        if str(text)!="None":
            #text
            text=re.sub(r"\s+", " ", text)
            #created_at
            created=data.get('created_at')
            if type(created)=='unicode':
                created=created.encode('utf-8')
            user=data.get('user')          
            if user is not None:
                user_id=user.get('id_str')
                if type(user_id)=='unicode':
                    user_id=user_id.encode('utf-8')
                user_id="["+user_id+"]"
                location=user.get('location')
                if type(location)=='unicode':
                    location=location.encode('utf-8')

            lang=data.get('lang')
            if type(lang)=='unicode':
                lang=lang.encode('utf-8')

            if all(map(lambda w: w in text.lower(),(word1,word2,word4))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word1,word3,word5))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word1,word2))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word1,word3))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word1,word4))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word1,word5))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word2,word4))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word2,word5))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word3,word4))):
                txt_about="ALL"
            elif all(map(lambda w: w in text.lower(),(word3,word5))):
                txt_about="ALL"
            elif word1 in text.lower():
                txt_about=word1
            elif word2 in text.lower():
                txt_about=word2
            elif word3 in text.lower():
                txt_about=word2
            elif word4 in text.lower():
                txt_about=word4
            elif word5 in text.lower():
                txt_about=word4
            else:
                txt_about="none"
            if(txt_about is not "none"):

                blob = TextBlob(data.get("text"))
                sentnumb=blob.sentiment.polarity
                if sentnumb < 0:
                    sentiment = "negative"
                elif sentnumb == 0:
                    sentiment = "neutral"
                else:
                    sentiment = "positive"
                each_tw.append(count)
                count=count+1
                each_tw.append(created)
                each_tw.append("["+str(location)+"]")
                each_tw.append(user_id)
                each_tw.append(lang)
                each_tw.append(sentnumb)
                each_tw.append(sentiment)
                each_tw.append(txt_about)
                tw_array.append(each_tw)
    tw_array=pd.DataFrame(tw_array)

    df = pd.DataFrame(tw_array)
    df.columns = ['key','created', 'location', 'user_id',"lang","sentinumb","sentiment","txt_about"]
    with open("LAB/"+direct+"/main.csv", 'a') as f:
        df.to_csv(f,index=None,encoding='utf-8')