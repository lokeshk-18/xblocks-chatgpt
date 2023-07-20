from django.conf import settings as django_settings

SETTINGS_KEY = 'xblocks-chatgpt'

DEFAULT_SETTINGS = {
    "display_name": "Camped XBlock",
}

def get_xblock_settings():
    try:
        xblock_settings = django_settings.XBLOCK_SETTINGS
    except AttributeError:
        settings = DEFAULT_SETTINGS
    else:
        settings = xblock_settings.get(
            SETTINGS_KEY, DEFAULT_SETTINGS)

    return settings