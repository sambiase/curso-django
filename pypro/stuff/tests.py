import pytest
# from django.test import TestCase
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('stuff:video', args=('Binance_BEP20',)))  # args eh o SLUG da app


def test_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp):
    assert_contains(resp, '<h1>Binance BEP20</h1>')


def test_video_contents(resp):
    assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/eOn7RuaYANk"')
