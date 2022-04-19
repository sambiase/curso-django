import pytest
# from django.test import TestCase
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('stuff:video', args=('Binance_BEP20',)))  # args eh o SLUG da app


def test_status_code(resp):
    assert resp.status_code == 200
