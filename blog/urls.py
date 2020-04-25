from django.urls import path
from . import views
# importamos la url desde django.urls
urlpatterns = [
    path('', views.post_list, name='post_list'),
]