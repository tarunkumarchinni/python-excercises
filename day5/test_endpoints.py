import pytest

import requests



url = 'http://127.0.0.1:5000' # The root url of the flask app



def test_index_page():

    r = requests.get(url + '/')

    assert r.status_code == 200



def test_get_customer():

    r = requests.get(url + '/register')
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0

def test_get_updatedaccount():

    r = requests.get(url + '/updateaccount/tc123')
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0

def test_get_updatedaccount_detail():

    r = requests.get(url + '/updateaccount/avc123')

    assert r.status_code == 200

    data = r.json()

    assert len(data) > 0




def test_no_customer():

    r = requests.get(url + '/updateaccount/tc1123')

    assert r.status_code == 404