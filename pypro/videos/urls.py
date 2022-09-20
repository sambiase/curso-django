from django.urls import path
from pypro.videos.views import video, index

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),  # '' raiz do projeto, home = funcao home criada no passo anterior
    path('', index, name='index'),
]
