import os
import numpy as np
import pandas as pd
import csv
import codecs
import tweepy
import json
import codecs
import collections
import re
import sys


directory = os.listdir('LAB/vir_result/user_follow')
del directory[0]
for filename in directory:
	cell=[]
	filename = filename.replace('.csv', '')
	cell.append(filename)
	u = api.get_user(int(filename))
	html_name="https://twitter.com/"+str(u.screen_name)
	cell.append(html_name)
	ar_follow.append(cell)
ar_follow=np.array(ar_follow)
ar_follow=ar_follow.transpose()
df=pd.DataFrame(ar_follow)
with open("LAB/vir_result/user_follow_name.csv", 'w') as f:
    df.to_csv(f,index=None,encoding='utf-8')

file1="LAB/vir_result/user_follow_name.csv"
with codecs.open(file1, "r", "Shift-JIS", "ignore") as f1:
    data_main = pd.read_table(f1, delimiter=",")

data_file=data_main['user_id']
data_result=data_main['result']
cat1_word=[]
cat2_word=[]
cat3_word=[]
cat4_word=[]
word_ar=[]
for i in range(len(data_main)):
	data_f = str(data_file[i])+'.csv'
	file2 = open("LAB/usa_election/result_vir_per/user_follow/"+data_f)
	reader=csv.reader(file2)
	if data_result[i]==1:
		for row in reader:
			cat1_word.append(row[1])
	elif data_result[i]==2:
		for row in reader:
			cat2_word.append(row[1])
	elif data_result[i]==3:
		for row in reader:
			cat3_word.append(row[1])
	elif data_result[i]==4:
		for row in reader:
			cat4_word.append(row[1])
cat1=[]
cat2=[]
cat3=[]
cat4=[]
word_ar=[]
unique1, counts1 = np.unique(cat1_word, return_counts=True)
for j in range(len(unique1)):
	if counts1[j]>5:
		cat1.append(unique1[j])
unique2, counts2 = np.unique(cat2_word, return_counts=True)
for j in range(len(unique2)):
	if counts2[j]>5:
		cat2.append(unique2[j])
unique3, counts3 = np.unique(cat3_word, return_counts=True)
for j in range(len(unique3)):
	if counts3[j]>5:
		cat3.append(unique3[j])
unique4, counts4 = np.unique(cat4_word, return_counts=True)
for j in range(len(unique4)):
	if counts4[j]>5:
		cat4.append(unique4[j])
len_max=max(len(cat1),len(cat2),len(cat3),len(cat4))
if len(cat1) is not len_max:
	l_dis=len_max-len(cat1)
	for m in range(l_dis):
		cat1.append('')
if len(cat2) is not len_max:
	l_dis=len_max-len(cat2)
	for m in range(l_dis):
		cat2.append('')
if len(cat3) is not len_max:
	l_dis=len_max-len(cat3)
	for m in range(l_dis):
		cat3.append('')
if len(cat4) is not len_max:
	l_dis=len_max-len(cat4)
	for m in range(l_dis):
		cat4.append('')	
word_ar=[]
word_ar.append(cat1)
word_ar.append(cat2)
word_ar.append(cat3)
word_ar.append(cat4)
word_ar=np.array(word_ar)
word_ar=word_ar.transpose()
df=pd.DataFrame(word_ar)
with open("LAB/vir_result/user_countfollow.csv", 'w') as f:
    df.to_csv(f,index=None,encoding='utf-8')
