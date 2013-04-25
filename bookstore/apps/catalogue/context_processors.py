from django.conf import settings


def defaults(request):
    return {
        'about_us_image': settings.ABOUT_US_DEFAULT_IMAGE
    }