from random import randrange
import requests
import json
import re 
import pprint
import time

def get_Response(html_url,params=None):
    headers={
        "Referer": "https://max.book118.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36"
        }
    response=requests.get(html_url,headers=headers,params=params)
    return response

def save_png(png_url,png_name):
    response=get_Response(png_url)
    with open(png_name,"wb") as f:
        f.write(response.content) 

html_url="https://openapi.book118.com/getPreview.html"
png_url_list=[]

for page in range(1,24,6):
    params={
        "project_id": "1",
        "aid": "354607192",
        "view_token": "HjXCVKRHT4l_IQyz9cnzs9nffOPCKQPQ",
        "page": page
    }
    response=get_Response(html_url=html_url,params=params)
    data=re.findall('jsonpReturn\((.*?)\);',response.text)[0]
    json_data=json.loads(data)["data"]
    for i in json_data.items():
        png_url="https:"+i[1]
        png_url_list.append(png_url)
    time.sleep(2)

i=1
dir_name="F:\\pythoncode\\spider_test\\Maxbook\\png1\\"
for png_url in png_url_list:
    png_name=dir_name+str(i)+".png"
    save_png(png_url=png_url,png_name=png_name)
    i=i+1

# pprint.pprint(json_data)