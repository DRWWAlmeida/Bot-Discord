from django.shortcuts import render
from django.http import HttpResponse, Http404
from web.models import Event
from django.contrib.auth.decorators import login_required
from discordbot.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def home(request):
    if request.method == "GET":
        return render(request, 'web/pages/register_event.html')
    elif request.method == "POST":
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        event_message = request.POST.get('event_message')
        author = request.user
        new_event = Event(event_name=event_name, event_date=event_date, event_time=event_time, event_message=event_message, author=author)
        new_event.save()
        # HttpResponse('Dados salvos no banco de dados')
        return render(request, 'web/pages/register_event.html', context={'saved': True})
    else:
        # HttpResponse('Algo deu errado')
        return render(request, 'web/pages/register_event.html', context={'saved': False})


def events(request):
    events_list = Event.objects.all()
    return render(request, 'web/pages/events.html', context={
        'events_list': events_list,
    })
