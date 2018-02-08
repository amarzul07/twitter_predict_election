#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 07:58:15 2017
user: cross sentiment and txt_about
@author: amarzulgantumur
"""
import pandas as pd
import numpy as np
import codecs
import collections

direct="vir_result"
for i in range(1):
    data_array=[]
    file1="/Users/amarzulgantumur/LAB/"+direct+"/user_res_naive1.csv"
    with codecs.open(file1, "r", "Shift-JIS", "ignore") as f1:
        data_main = pd.read_table(f1, delimiter=",")
    f1.close()
    if(len(np.array(data_main))>0):
        data_origin=data_main.drop_duplicates(['user_id'],keep='last')
        data_origin=data_main.ix[data_main["predicted"]==0]
        #data_main.to_csv("LAB/"+direct+"/nonesarcasm_ALL.csv")
        #data_origin=pd.merge(data_main,data_sarcasm,on="key")
        #data_origin=data_main
        #data_origin['sent_next']=data_origin['sentiment']
        #mask1=((data_origin["predicted"]==1) & (data_origin["sentiment"] is "negative"))
        #mask2=((data_origin["predicted"]==1) & (data_origin["sentiment"] is not "negative"))
        #column_name='sent_next'
        #data_origin.ix[mask1,column_name]="positive"
        #data_origin.ix[mask2,column_name]="negative"

        #data_origin.to_csv("LAB/kenya_election/result/"+fname+"_ALL.csv")
        #from_d="jer"
        #data=data_origin.ix[data_origin["txt_from"]=="jersey"]
        #data_main=data_main.ix[data_main["sent"]=="['positive']"]
        data_loc=data_origin['location']
        data_loc_ar=np.array(data_loc)
        
        data_id=data_origin['user_id']
        data_id_ar=np.array(data_id)
        
        data_lang=data_origin['lang']
        data_lang_ar=np.array(data_lang)
        
        #data_snumb=data_origin['sentinumb']
        #data_snumb_ar=np.array(data_snumb)
        
        data_sent=data_main['sent_naive']
        data_sent_ar=np.array(data_sent)
        
        data_about=data_main['txt_about']
        data_about_ar=np.array(data_about)

        
        data_from=data['txt_from']
        data_from_ar=np.array(data_from)
        user_id
        
        counter_loc=collections.Counter(data_loc_ar)
        counter_id=collections.Counter(data_id_ar)
        counter_lang=collections.Counter(data_lang_ar)
        counter_from=collections.Counter(data_from_ar)

        data_array=[]
        data_array.append(counter_loc.most_common(5))
        data_array.append(counter_id.most_common(5))
        data_array.append(counter_lang.most_common(5))
        data_array.append(counter_from.most_common(5))
        
        df_data = pd.DataFrame(data_array)
        df_data.to_csv("LAB/"+direct+"/user_count.csv")

        df=[]       
        df=pd.DataFrame({'Sent_naive':data_sent_ar,
                          'About':data_about_ar})

        cr=[]
        cr=df.pivot_table(index='Sent_naive',columns='About',aggfunc=[len],fill_value=0)
        cr.to_csv("LAB/"+direct+"/sar_res.csv",encoding="SHIFT-JIS")
