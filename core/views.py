from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class AudioView(View):
    def get(self, request):
        return render(request, 'blog/single-audio.html')

class GalleryView(View):
    def get(self, request):
        return render(request, 'blog/single-gallery.html')

class VideoView(View):
    def get(self, request):
        return render(request, 'blog/single-video.html')

class StandardView(View):
    def get(self, request):
        return render(request, 'blog/single-standard.html')

class DiaryView(View):
    def get(self, request):
        return render(request, 'blog/single-diary.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class StyleView(View):
    def get(self, request):
        return render(request, 'style-guide.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')