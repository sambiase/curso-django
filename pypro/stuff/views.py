from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'CryptotechBr: Binance BEP20', 'youtube_id': 'eOn7RuaYANk'}
    return render(request, 'stuff/video.html', context={'video': video})
