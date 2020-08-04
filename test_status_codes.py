import setting
import requests
import pytest
from helper_function import check_content_type

@pytest.mark.parametrize(
    "code, result",
    [(200, 200),
     (302, 200),
     (400, 400),
     (999, 999),
     (422, 422)
     ])
def test_get_status_codes_default(code, result):
    url = setting.DOMEN_NAME + '/status/' + str(code)
    r = requests.get(url)
    assert r.status_code == result, f"Неверный код ответа: {r.status_code}"


@pytest.mark.parametrize(
    "code, result",
    [(104, 104),
     (209, 209),
     (302, 200),
     (402, 402)
     ])
def test_post_status_codes(code, result):
    url = setting.DOMEN_NAME + '/status/' + str(code)
    r = requests.post(url)
    assert r.status_code == result, f"Неверный код ответа: {r.status_code}"


@pytest.mark.parametrize(
    "code, result",
    [(204, 204),
     (209, 209),
     (400, 400),
     (500, 500)
     ])
def test_put_status_codes(code, result):
    url = setting.DOMEN_NAME + '/status/' + str(code)
    r = requests.put(url)
    assert r.status_code == result, f"Неверный код ответа: {r.status_code}"


@pytest.mark.parametrize(
    "code, result",
    [(404, 404),
     (202, 202),
     (422, 422),
     (502, 502)
     ])
def test_patch_status_codes(code, result):
    url = setting.DOMEN_NAME + '/status/' + str(code)
    r = requests.patch(url)
    assert r.status_code == result, f"Неверный код ответа: {r.status_code}"


@pytest.mark.parametrize(
    "code, result",
    [(405, 405),
     (209, 209),
     (999, 999),
     (102, 102),
     (503, 503)
     ])
def test_delete_status_codes(code, result):
    url = setting.DOMEN_NAME + '/status/' + str(code)
    r = requests.delete(url)
    assert r.status_code == result, f"Неверный код ответа: {r.status_code}"


@pytest.mark.parametrize(
    "method,code",
    [('GET', 405),
     ('POST', 209),
     ('PUT', 999),
     ('PATCH', 102),
     ('DELETE', 503)
     ])
def test_check_content_type_method_status_code(method, code):
    url = setting.DOMEN_NAME + '/status/' + str(code)
    r = requests.request(method, url)
    assert check_content_type(r) == 'text/html', f"Неверный тип контента в ответ: {check_content_type(r)}"
