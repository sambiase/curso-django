from django.test import Client

from pypro.django_assertions import assert_contains


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200  # certificar que deu tudo certo

def test_home_title (client: Client):
    resp = client.get('/')
    assert_contains (resp, '<title>Curso Django!</title>')
