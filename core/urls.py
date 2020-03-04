from django.contrib import admin
from django.urls import path
from .views import HomeView, AudioView, DiaryView, GalleryView, StandardView, VideoView, AboutView, StyleView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('audio', AudioView.as_view(), name='audio'),
    path('diary', DiaryView.as_view(), name='diary'),
    path('gallery', GalleryView.as_view(), name='gallery'),
    path('standard', StandardView.as_view(), name='standard'),
    path('video', VideoView.as_view(), name='video'),
    path('about', AboutView.as_view(), name='about'),
    path('style', StyleView.as_view(), name='style'),
    path('contact', ContactView.as_view(), name='contact'),
]
