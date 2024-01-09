import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "discordbot.settings")
django.setup()
from web.models import Event


def events_consult():
    return Event.objects.filter(is_published=True)
