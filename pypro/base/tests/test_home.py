import pytest
from django.test import Client
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200  # certificar que deu tudo certo


def test_home_title(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Curso Django</a>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Curso Django</a>')
