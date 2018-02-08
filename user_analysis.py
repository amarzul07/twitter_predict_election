#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 07:58:15 2017

@author: amarzulgantumur
"""
import pandas as pd
import numpy as np
import codecs
import collections
direct="vir_result"
word1="gillespie"
word2="ralph"
word3="ALL"
user_sent = {
        'positive'    : 2,
        'negative'    : -1,
        'neutral' : 1
}
user_about = {
        word1    : 0,
        word2    : 1,
        word3    : 2
}
for i in range(1):
    fname="nonesarcasm_ALL.csv"
    data_array=[]
    file1="LAB/"+direct+"/"+fname
    with codecs.open(file1, "r", "Shift-JIS", "ignore") as f1:
        data_main = pd.read_table(f1, delimiter=",")
    f1.close()
    if(len(np.array(data_main))>0):
        data_user=data_main.drop_duplicates(['user_id'],keep='last')
        data_id=data_user['user_id']
        data_id_ar=np.array(data_id)
        
        user_res=[]
        for userid in data_id_ar:
            user_per=[]
            user_p=[]
            user1=0
            user2=0
            user3=0
            user4=0
            user5=0
            user6=0
            data=data_main.ix[data_main["user_id"]==userid]
            if len(data)==1:
                data_sent=data['sent_naive']
                data_sent=np.array(data_sent)
                data_about=data['txt_about']
                data_about=np.array(data_about)
                if data_about[0]==word1:
                    if data_sent[0]=="positive":
                        user1=user1+1
                    elif data_sent[0]=="negative":
                        user2=user2+1
                    else:
                        user3=user3+1
                elif data_about[0]==word2:
                    if data_sent[0]=="positive":
                        user4=user4+1
                    elif data_sent[0]=="negative":
                        user5=user5+1
                    else:
                        user6=user6+1
                else:
                    if data_sent[0]=="positive":
                        user1=user1+1
                        user4=user3+1
                    elif data_sent[0]=="negative":
                        user2=user2+1
                        user5=user4+1
                    else:
                        user3=user2+1
                        user6=user4+1
            else:
                data_sent=data['sent_naive']
                data_sent_ar=np.array(data_sent)
                    
                data_about=data['txt_about']
                data_about_ar=np.array(data_about)
                        
                for num in range(len(data_about_ar)):
                    if data_about_ar[num]==word1:
                        if data_sent_ar[num]=="positive":
                            user1=user1+1
                        elif data_sent_ar[num]=="negative":
                            user2=user2+1
                        else:
                            user3=user3+1
                    elif data_about_ar[num]==word2:
                        if data_sent_ar[num]=="positive":
                            user4=user4+1
                        elif data_sent_ar[num]=="negative":
                            user5=user5+1
                        else:
                            user6=user6+1
                    else:
                        if data_sent_ar[num]=="positive":
                            user1=user1+1
                            user4=user3+1
                        elif data_sent_ar[num]=="negative":
                            user2=user2+1
                            user5=user4+1
                        else:
                            user3=user2+1
                            user6=user4+1
            user_per.append(userid)
            user_per.append(user1)
            user_per.append(user2)
            user_per.append(user3)
            user_per.append(user4)
            user_per.append(user5)
            user_per.append(user6)
            user_p.append(user1)
            user_p.append(user2)
            user_p.append(user3)
            user_p.append(user4)
            user_p.append(user5)
            user_p.append(user6)
            user_max=np.amax(user_p)
            user_ab=[user1+user2+user3,user4+user5+user6]
            user_ab_max=np.amax(user_ab)
            if user_ab_max==user1+user2+user3:
                txt_about=word1
                if user_max==user1:
                    sent="positive"
                elif user_max==user2:
                    sent="negative"
                else:
                    sent="neutral"
            elif user_ab_max==user4+user5+user6:
                txt_about=word2
                if user_max==user4:
                    sent="positive"
                elif user_max==user5:
                    sent="negative"
                else:
                    sent="neutral"
            user_per.append(txt_about)
            user_per.append(sent)
            user_res.append(user_per)
    
df = pd.DataFrame(user_res)
df.columns = ['userid',word1+'-pos',word1+'-neg',word1+'-neu',word2+'-pos',word2+'-neg',word2+'-neu',"txt_about","sent"]
with open("LAB/"+direct+"/none_user_res.csv", 'w') as f:
    df.to_csv(f,index=None,encoding='utf-8')