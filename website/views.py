from django.shortcuts import render
from django.http import HttpResponse
from .models import topic
from django_user_agents.utils import get_user_agent

# Create your views here.


def hello(request):

    return HttpResponse('<<<<<<<<<<<<<<<<<<<<<< HELLOOOOOOOOOOOOOOOOOOOOOOOOOO WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORLD >>>>>>>>>>>>>')

def shortview(request):

    topics=topic.objects.all().order_by('-uploaded_on')


    user_agent=get_user_agent(request)
    if user_agent.is_mobile:
        return render(request,'mobile/shortview.html',{'topics':topics})
    else:
        return render(request,'shortview.html',{'topics':topics})
def detailview(request,id):
    topic_id=id
    topics=topic.objects.get(pk=topic_id)

    user_agent=get_user_agent(request)
    if user_agent.is_mobile:
        return render(request,'mobile/detailview.html',{'topics':topics})
    else:
        return render(request,'detailview.html',{'topics':topics})


def documentview(request):
    topics=topic.objects.all().order_by('-uploaded_on')


    user_agent=get_user_agent(request)
    if user_agent.is_mobile:
        return render(request,'mobile/documentview.html',{'topics':topics})
    else:
        return render(request,'documentview.html',{'topics':topics})
