from www import settings

def static_template_vars(context):
    return {
            'MEDIA_URL': settings.MEDIA_URL,
            'RESOURCES_URL': settings.RESOURCES_URL,
            }