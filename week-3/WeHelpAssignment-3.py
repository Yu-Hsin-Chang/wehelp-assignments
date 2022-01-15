
# coding: utf-8

# In[108]:


import urllib.request as req
import json
import re
import csv
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
request = req.Request(url)
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
sitedata = json.loads(data)

# 輸出cvs資料
Totalarray = []
for content in sitedata['result']['results']: 
        array = []
        array.append(content['stitle'])
        array.append(content['address'][4:8].replace(" ",""))
        array.append(content['longitude'])
        array.append(content['latitude'])
        array.append(content['file'].lower().split(".jpg")[0]+'.jpg')  
        Totalarray.append(array)
print(Totalarray)
with open('assignment03_data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  # 寫入二維表格
  writer.writerows(Totalarray)


# In[109]:




