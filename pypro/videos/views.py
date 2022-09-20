from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, title, youtube_id):
        self.slug = slug
        self.title = title
        self.youtube_id = youtube_id

    def get_absolute_url(self):
        return reverse('videos:video', args=(self.slug,))

videos = [
    # http://127.0.0.1:8000/videos/Binance_Bep20
    Video('Binance_Bep20', 'Binance_Bep20', 'vO_BGXQFwo4'),
    # http://127.0.0.1:8000/videos/Trust_Wallet
    Video('Trust_Wallet', 'Trust_Wallet', '-vJHYb1JLws')
]
videos_dct = {v.slug: v for v in videos}


def index(request):
    return render(request, 'videos/index.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'videos/video.html', context={'video': video})
