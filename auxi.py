import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "discordbot.settings")
django.setup()
from web.models import Event  # type: ignore

events = Event.objects.filter(is_published=True)
for i in events:
    print(i.event_name)
    print(i.event_date)
    print(i.event_time)
    print(i.event_message)
