import setting
import requests
from helper_function import check_content_type


def test_check_headers_status_codes():
    url = setting.DOMEN_NAME + '/headers'
    r = requests.get(url)
    print(r.status_code)
    assert r.status_code == 200, f"Неверный код ответа: {r.status_code}"


def test_check_headers_content_type():
    url = setting.DOMEN_NAME + '/headers'
    r = requests.get(url)
    assert check_content_type(r) == 'application/json', f"Неверный тип котента в ответе: {check_content_type(r)}"


def test_check_headers_body():
    url = setting.DOMEN_NAME + '/headers'
    r = requests.get(url)
    if r.headers['Content-Type'] == 'application/json':
        assert 'headers' in r.json()
    else:
        assert False, "не правильный формат ответа"
