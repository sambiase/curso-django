import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('videos:index'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'title', [
        'Binance_Bep20',
        'Trust_Wallet'
    ]
)
def test_video_title(resp, title):
    assert_contains(resp, title)


@pytest.mark.parametrize(
    'slug', [
        'Binance_Bep20',
        'Trust_Wallet'
    ]
)
def test_video_link(resp, slug):
    video_link = reverse('videos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')



# def test_video_content(resp):
#     assert_contains(resp, '<iframe src="https://www.youtube.com/embed/vO_BGXQFwo4"')
