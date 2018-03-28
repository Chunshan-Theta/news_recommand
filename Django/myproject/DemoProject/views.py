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
        eachdiv["title"] = i[6]
        eachdiv["picbiref"] = i[7]
        eachdiv["picurl"] = i[8]
        arr.append(eachdiv)

    template = 'index.html'
    responds = {'Data':arr}
    return render(request,template,responds )
def SQL_test(request,c):
    md.connectDB()
    a = md.exeSQl('SELECT *,count(DISTINCT `url`) FROM `PostList` GROUP BY `url` ORDER BY `PostList`.`id` ASC')
    #a = md.exeSQl('SELECT * FROM `PostList`')

    md.close()
    cpint =int(c)
    for i in range(200):
        if str(a[i][0]) == str(cpint):
            cpint = i
            break

    
    criteria_point = a[cpint][3]    
    import json    
    criteria_point_j = json.loads(criteria_point)
    text_array=[]
    text_array_extent=[]
    opener_div =[]    
    opener_div.append(a[cpint][1])
    opener_div.append(a[cpint][5])
    opener_div.append(a[cpint][2]+"   ,"+str(a[cpint][0]))
    text_array.append(opener_div)
    text_array.append(["ㄧ個月內相關文章"])
    index=0

    while len(text_array)<10+1 and index <1000:
        
        if index == cpint:
            index+=1    
        score=0
        test_point = a[index][3]
        try:
            test_point_j = json.loads(test_point)
        except:
            print(test_point)
        for i in range(20):
            for j in range(20):
                try:
                    cx = float(criteria_point_j[str(i)+'-x']) 
                    cy = float(criteria_point_j[str(i)+'-y'])
                    tx = float(test_point_j[str(j)+'-x'])
                    ty = float(test_point_j[str(j)+'-y']) 
                    
                    result = ((tx-cx)**2+(ty-cy)**2)**0.5
                    if result==0:
                        score+=1
                        break
                    elif result<0.000000005 and i<=5 and j<=5:
                        score+=0.5
                        break
                    else:
                        pass
                except:
                    pass
                    
        if score>=7.5:
            news_div=[]
            news_div.append(str(a[index][0])+","+str(score)+","+a[index][2])
            news_div.append(a[index][1])
            news_div.append(str(a[index][5]))
            text_array.append(news_div)
        elif score>=4.5 and len(text_array_extent)<20:
            news_div=[]
            news_div.append(str(a[index][0])+","+str(score)+","+a[index][2])
            news_div.append(a[index][1])
            news_div.append(str(a[index][5]))
            text_array_extent.append(news_div)
        else:
            pass
        index+=1
    else:
        text_array.append(["Search_end:"+str(index)])
    #print(text_array)
    template = 'news_each.html'
    responds = {'Data':text_array,"Data2":text_array_extent}
    return render(request,template,responds )
