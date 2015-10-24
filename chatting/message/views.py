from django.shortcuts import render
from message.models import Message
from django.http import HttpResponse
import json


# Create your views here.
def list(request):
    messages = []
    for data in Message.objects.all().order_by('id'):
            dic = {}
            dic['sender'] = data.sender
            dic['datetime'] = data.datetime
            dic['content'] = data.content
            messages.append(dic)

    return render(
        request,
        'message/list.html',
        {'messages': messages},
    )


def message(request, last_update_time=None):
    if request.method == 'POST':
        Message.objects.create(
            sender=request.POST.get('sender', ''),
            content=request.POST.get('content', ''),
        )
        return HttpResponse("inserted")

    elif request.method == 'GET':
        if last_update_time is None:
            last_update_time = request.GET.get('last_update_time', None)

        if last_update_time is not None:
            messages = []
            for data in Message.objects.all().order_by('id'):
                    dic = {}
                    dic['sender'] = data.sender
                    dic['datetime'] = str(data.datetime)
                    dic['content'] = data.content
                    messages.append(dic)
            messages = json.dumps(messages)
            return HttpResponse(messages, content_type='application/json')

    return HttpResponse("error")
