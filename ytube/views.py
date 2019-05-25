from django.shortcuts import render
import requests
import json


# Create your views here.
from . import models

class DataList(SelectRelatedMixin, generic.ListView):
    model = models.YTdata
    search = models.YTdata


def youtube_api():
    temp3=[]
    q=requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&order=viewCount&publishedAfter=2019-01-01T00%3A00%3A00Z&q={{search}}&type=video&videoDefinition=high&key=AIzaSyBlhx-ghTGYAHjzfuggysAgjPwOZInXgJc')
    if q.status_code == 200:
        q=q.json()
        data1 = q['items']

        for j in data1:
            temp2={}
            c = j['snippet']
            contentx = c['thumbnails']
            std = contentx['medium']
            res_id = j['id']
            temp2.update({'youtube_url':std['url']})
            temp2.update({'youtube_title':c['title']})
            temp2.update({'youtube_id':res_id['videoId']})
           
    temp2['youtube_url'] = YTdata.objects.get(id = title)

