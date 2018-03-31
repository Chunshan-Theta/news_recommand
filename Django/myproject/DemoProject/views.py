# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sys
sys.path.append('/home/gavin/Desktop/news_recommand/Django/myproject/DemoProject/models/')
import MySQL_model as md
###### show view ######

def hello_world(request):
    template = 'hello_world.html'
    responds = {'stringData': str(datetime.now()),}
    return render(request,template,responds )


def UsingStaticSource(request):
    template = 'UsingStaticSource.html'
    responds = {}
    return render(request,template,responds )

def For_Cycle(request):
    template = 'For_Cycle.html'
    arr = [1,2,3,4,5,6,7,8,9]
    responds = {'Data':arr}
    return render(request,template,responds )

def Http_From_Get(request,input1,input2):
    template = 'hello_world.html'
    responds = {'stringData': str(input1)+str(input2),}
    return render(request,template,responds )

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def Http_From_Post(request):
    try:
        data = str(request.POST['input1'])
    except KeyError as e:
        data = 'did not have post'


    template = 'Form.html'
    responds = {'stringData': data,}
    return render(request,template,responds )

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def api_template(request):
    try:
        data = str(request.POST['input1'])
    except KeyError as e:
        data = 'did not have post'


    resp = HttpResponse(data)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp 
def SQL_all(request):
    
    md.connectDB()
    a = md.exeSQl('SELECT *,count(DISTINCT `url`) FROM `PostList` GROUP BY `url` ORDER BY `PostList`.`id` ASC Limit 50')
    #a = md.exeSQl('SELECT * FROM `PostList`')

    md.close()

    arr=[]

    for i in a:
        eachdiv={}
        eachdiv["id"] = i[0]
        eachdiv["content"] = i[1][:100]
        eachdiv["keywords"] = i[5]
        eachdiv["url"] = i[2]
        eachdiv["title"] = i[6][:20]
        eachdiv["picbiref"] = i[7]
        eachdiv["picurl"] = i[8]
        arr.append(eachdiv)

    template = 'news_list.html'
    responds = {'Data':arr}
    return render(request,template,responds )
def SQL_test(request,c):
    md.connectDB()
    a = md.exeSQl('SELECT *,count(DISTINCT `url`) FROM `PostList` GROUP BY `url` ORDER BY `PostList`.`id` ASC')
    #a = md.exeSQl('SELECT * FROM `PostList`')

    md.close()
    cpint =int(c)
    for i in reversed(range(int(cpint)+1)):
        if str(a[i][0]) == str(cpint):
            cpint = i
            #print(i)
            break

    
    criteria_point = a[cpint][3]    
    import json    
    criteria_point_j = json.loads(criteria_point)
    opener_div ={}    
    opener_div["id"] = a[cpint][0]
    opener_div["content"] = a[cpint][1]
    opener_div["keywords"] = a[cpint][5]
    opener_div["url"] = a[cpint][2]
    opener_div["title"] = a[cpint][6][:20]
    opener_div["picbiref"] = a[cpint][7]
    opener_div["picurl"] = a[cpint][8]
    opener_div["date"] = a[cpint][4]

    
    text_array=[]
    index=0
    top10_index=[]
    top10_div=[]
    #print(len(a))
    while index <3000 and index <len(a)-1:
        
        if index == cpint:
            index+=1    
        
        test_point = a[index][3]
        try:
            test_point_j = json.loads(test_point)
        except:
            print(test_point)


        score=0
        for i in range(20):
            each_score=[]
            for j in range(20):
                try:
                    cx = float(criteria_point_j[str(i)+'-x']) 
                    cy = float(criteria_point_j[str(i)+'-y'])
                    tx = float(test_point_j[str(j)+'-x'])
                    ty = float(test_point_j[str(j)+'-y']) 
                    
                    result = ((tx-cx)**2+(ty-cy)**2)**0.5
                    each_score.append(1-result)
                    
                except:
                    pass
            score += max(each_score)
                    
        text_array.append([score,index])
        index+=1
    else:
        
        for i in range(9):
            #print(max(text_array)[1])
            top10_index.append(max(text_array)[1])
            del text_array[text_array.index(max(text_array))]
    #print(text_array)
    for i in top10_index:
        eachdiv={}
        eachdiv["id"] = a[i][0]
        eachdiv["content"] = a[i][1][:100]
        eachdiv["keywords"] = a[i][5]
        eachdiv["url"] = a[i][2]
        eachdiv["title"] = a[i][6]
        eachdiv["picbiref"] = a[i][7]
        eachdiv["picurl"] = a[i][8]

        top10_div.append(eachdiv)

    template = 'news_each.html'
    responds = {'Topic':opener_div,'Data':top10_div}
    return render(request,template,responds )
