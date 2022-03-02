from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core.views import Home, ProfileList, ProfileCreate, Watch, ShowMovieDetail, ShowMovie

app_name = 'core'

urlpatterns = [
    path('', Home.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/', Watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name='show_detail'),
    path('movie/play/<str:movie_id>', ShowMovie.as_view(), name='play'),
]