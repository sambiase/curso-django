from django.shortcuts import render


def video(request, slug):
    return render(request, 'stuff/video.html')
