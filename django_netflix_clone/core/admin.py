from django.contrib import admin
from core.models import Movie, Profile, CustomUser, Video

# Register your models here.
admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(CustomUser)
