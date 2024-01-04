from django.shortcuts import render
from django.http import HttpResponse, Http404


def home(request):
    if request.method == "GET":
        return render(request, 'web/pages/home.html')
    elif request.method == "POST":
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        event_message = request.POST.get('event_message')
        return HttpResponse(event_name + event_date + event_message)
    else:
        return HttpResponse('Algo deu errado')
 