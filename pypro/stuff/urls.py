from django.urls import path

from pypro.stuff.views import video

app_name = 'stuff'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
# <slug> comes from file tests.py
# view video comes from views.py
