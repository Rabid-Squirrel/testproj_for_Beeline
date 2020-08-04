import setting
import requests
import pytest
from helper_function import check_content_type


@pytest.mark.parametrize(
    "n", [1, 2, 3, 10, 20])
def test_check_redirect_n_status_code(n):
    url = setting.DOMEN_NAME + '/redirect/' + str(n)
    r = requests.get(url)
    for resp in r.history:
        assert resp.status_code == 302, f"Неверный код ответа: {resp.status_code}"

@pytest.mark.parametrize(
    "n", [1, 10])
def test_check_redirect_n_content_type(n):
    url = setting.DOMEN_NAME + '/redirect/' + str(n)
    r = requests.get(url)
    for resp in r.history:
        assert check_content_type(resp) == 'text/html', 'тип контента не совпадает'


@pytest.mark.parametrize(
    "n", [1, 2, 3, 10, 20])
def test_check_redirect_n_count_times(n):
    url = setting.DOMEN_NAME + '/redirect/' + str(n)
    r = requests.get(url)
    assert len(r.history) == n, f"Количество редиректов не совпадает"


@pytest.mark.parametrize(
    "n", [1, 2, 3, 10, 20])
def test_check_redirect_n_url(n):
    url = setting.DOMEN_NAME + '/redirect/' + str(n)
    r = requests.get(url)
    for resp in r.history:
        if resp.url.split('/')[-1] == str(n):
            assert resp.url.split('/')[-2] == 'redirect' and resp.url.split('/')[-1] == str(n),"неверный url редиректа"
        else:
            assert resp.url.split('/')[-2] == 'relative-redirect',"неверный url редиректа"
