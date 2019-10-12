from django.shortcuts import render
from django.http import HttpResponse
from student.models import question
import json
import facebook

ACCESS_TOKEN = "EAAg3A6Nc3CoBANUTA51uyFVyhtRGo3SFziEwYioQsx5b1iOP9Ad3EavNFcGvjf9ROECsoidswZBcSHt3z4yz6zdPShUY408wKNOpZAxSTwgPQWT6Ip6SZCyTnreFPY1ujmF3xukK06z99wituMUcQZC6A6mFoX7qxH8aSsZBffiwWSukhp0NsMj6B1FTWCWywq4WMOMd22QZDZD"

def main(request):
    token = ACCESS_TOKEN
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('3784083104953929',fields='feed')
    context={}
    b=profile['feed']
    c=b['data']
    # context['a']=c
    # x=len(c)
    # context['a']=c[0]['message']
    # d=c[2]['message']
    # print(d)
    s = ''
    for i in range(len(c)-1):
        p = question(id_1=c[i]['id'], message=c[i]['message'], comment=2, updated_date="2019-11-11")
        p.save()
        i=i+1
    
    return render(request, 'homepage.html', context)





# for person in c:
#     print(person['id'])

 


    # context['a']=c
    # return render(request, 'homepage.html', context)
    





# Create your views here.
