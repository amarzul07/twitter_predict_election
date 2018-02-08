import requests
import pandas as pd
import numpy as np
import codecs
import collections

direct="vir_result"
file1="LAB/"+direct+"/user_about.csv"

with codecs.open(file1, "r", "Shift-JIS", "ignore") as f1:
    data_main = pd.read_table(f1, delimiter=",")

data_img=data_main['images']
data_img=np.array(data_img)
data_id=data_main['user_id']
data_id=np.array(data_id)

for i in range(len(data_id)):
	url = data_img[i]
	if url is not "ERROR":
		user_id=data_id[i]
		response = requests.get(url)
		if response.status_code == 200:
			with open("LAB/vir_result/user_img/"+user_id+".png", 'wb') as f:
				f.write(response.content)