import requests
from assertpy.assertpy import assert_that
from lxml import etree
import wheel


def test_api_get():
    gourl = "https://reqres.in/api/users?page=2"
    resp = requests.get(gourl)
    assert resp.status_code == 200
    resp_dict = resp.json()
    print(resp_dict['page'])
    data_list = resp_dict['data']
    counter = 0
    for record in data_list:
        counter = counter + 1
        print(counter, "record is \n")
        for key in record:
            print("record", counter, "property name is ", key)
            print("record", counter, "property value is", record[key])

    assert counter == 6


def test_api_post():
    gourl = "https://reqres.in/api/users"
    request_data = {
        'name': 'cool getter',
        'job': 'all rounder'
    }
    resp = requests.post(gourl,data=request_data)
    resp_data = resp.json()
    print(resp_data)
    assert resp.status_code == 201
    assert_that(resp_data['id']).is_not_none()

