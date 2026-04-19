from django.shortcuts import render, get_object_or_404
from .models import Video

# homepage
def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})


# video player page
def video_detail(request, id):
    video = get_object_or_404(Video, id=id)
    return render(request, 'video_detail.html', {'video': video})