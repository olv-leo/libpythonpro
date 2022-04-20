from unittest.mock import Mock

import pytest as pytest

from libpythonpro import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('olv-leo')
    assert avatar_url == url

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/57156836?v=4'
    resp_mock.json.return_value = {
        'login': 'olv-leo', 'id': 57156836,
        'avatar_url': url
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('olv-leo')
    assert 'https://avatars.githubusercontent.com/u/57156836?v=4' == url
