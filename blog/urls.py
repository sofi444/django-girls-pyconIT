from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # if someone enters 'http://127.0.0.1:8000/' -> post_list view
    # name='post_list' == name of view (can be the same or not)
]
