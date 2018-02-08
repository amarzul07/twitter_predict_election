import os
import numpy as np
import pandas as pd
import codecs
import collections
import csv

directory = os.listdir('LAB/vir_result/user_timeline')
del directory[0]
file1="LAB/vir_result/category_word.csv"
data_main=pd.read_csv(open(file1,'rU'), encoding='utf-8', engine='c')
data_cat1=data_main['cat1']
data_cat1=np.array(data_cat1)
data_cat2=data_main['cat2']
data_cat2=np.array(data_cat2)
data_cat3=data_main['cat3']
data_cat3=np.array(data_cat3)
data_cat4=data_main['cat4']
data_cat4=np.array(data_cat4)
word_count_ar=[]
count=[]

for filename in directory:
	count1=0
	count2=0
	count3=0
	count4=0
	cat_count=[]
	wwbp_count=[]
	f = open("LAB/vir_result/user_timeline"+filename)
	data = f.read()
	# counting
	for data_c in data_cat1:
		if data_c in data:
			count1=count1+1
	for data_c in data_cat2:
		if data_c in data:
			count2=count2+1
	for data_c in data_cat3:
		if data_c in data:
			count3=count3+1
	for data_c in data_cat4:
		if data_c in data:
			count4=count4+1
	wwbp_count.append(filename)
	cat_count.append(count1)
	cat_count.append(count2)
	cat_count.append(count3)
	cat_count.append(count4)
	cat_count=np.array(cat_count)
	cat_max=np.amax(cat_count)
	if count1==cat_max:
		wwbp_count.append(1)
	elif count2==cat_max:
		wwbp_count.append(2)
	elif count3==cat_max:
		wwbp_count.append(3)
	else:
		wwbp_count.append(4)
	word_count_ar.append(wwbp_count)

word_count_ar=pd.DataFrame(word_count_ar)
df = pd.DataFrame(word_count_ar)
with open("LAB/vir_result/user_count-cat.csv", 'w') as f:
    df.to_csv(f,index=None,encoding='utf-8')
