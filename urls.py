from django.urls import path
import Apps.views

app_name = 'Apps'

urlpatterns = [
    path('',Apps.views.like_post, name= 'like_post')


]
