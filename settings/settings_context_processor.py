from .models import Settings

from django.core.cache import cache


def get_settings(request):
    try:
        settings_data = cache.get('settings_data')
        print("New Cache")
    except Exception:
        print("New Data")
        settings_data = Settings.objects.last()
        cache.set("settings_data", settings_data, 60*60*24)
    # settings_data = Settings.objects.last()
    
    return {"settings_data": settings_data}