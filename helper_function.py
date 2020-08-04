import requests

def check_content_type(r:requests):
    return r.headers['Content-Type'].split(';')[0]
