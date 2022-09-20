import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(
        reverse('videos:video', args=('Binance_Bep20',)))  # Binance Bep20 is the slug that goes into urls.py <slug>


def test_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp):
    assert_contains(resp, 'Binance_Bep20')


def test_video_content(resp):
    assert_contains(resp, '<iframe src="https://www.youtube.com/embed/vO_BGXQFwo4"')
