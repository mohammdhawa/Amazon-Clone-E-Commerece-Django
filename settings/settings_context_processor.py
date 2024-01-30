from .models import Settings

from django.core.cache import cache


def get_settings(request):
    

    # check data in cache
    try:
        settings_data = cache.get('settings_data')
        print()
        print("*"*50, end='\n')
        print("Before any exceptino", settings_data)
    except Exception:
        print()
        print("*"*50, end='\n')
        print("An exception Error: ")
        settings_data = Settings.objects.last()
        cache.set('settings_data', settings_data, 60*60*24*30)
    
    return {"settings_data": settings_data}