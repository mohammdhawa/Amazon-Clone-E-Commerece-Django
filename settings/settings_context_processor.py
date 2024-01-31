from .models import Settings

from django.core.cache import cache


def get_settings(request):
    # Check data in cache
    # try:
    #     settings_data = cache.get('settings_data')
    #     print("*" * 50, end='\n')
    #     print("Cache hit:", settings_data)
    # except cache.DoesNotExist:
    #     print("*" * 50, end='\n')
    #     print("Cache miss: Exception caught")
    #     try:
    #         settings_data = Settings.objects.last()
    #         cache.set('settings_data', settings_data, 60*60*24*30)
    #     except Exception as e:
    #         print(f"An exception occurred while retrieving settings from the database: {e}")
    #         settings_data = None
    settings_data = Settings.objects.last()
    
    return {"settings_data": settings_data}