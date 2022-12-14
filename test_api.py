import requests
import pytest
import time

base_url = 'https://jsonplaceholder.typicode.com/'
HTTP_code = 200
url = 'https://playground.learnqa.ru/api/'

@pytest.mark.skip
def test_get_all_posts():
    response = requests.get(f'{base_url}posts')
    assert response.status_code == HTTP_code, 'wrong status code'
    assert len(response.json()) == 100, 'actual length does not match tj expected'
    #python -m pytest -s -v test_api.py - запустить тест

@pytest.mark.skip
def test_get_post1():
    response = requests.get(f'{base_url}posts/1')
    assert response.status_code == HTTP_code, 'wrong status code'
    response_data = response.json()
    # print(response_data)
    expected_keys = ['userId', 'id', 'title', 'body']
    for key in response_data.keys():
        assert key in expected_keys, 'wrong keys'

@pytest.mark.skip
def test_post_in_posts():
    post_data = {
        'id':101,
        'title': 'my title',
        'body': 'my body'
    }
    response = requests.post(f'{base_url}posts', data=post_data)
    assert response.status_code ==201, 'wrong code'
    response_data = response.json()
    expected_title = 'my title'
    #print(response.json())
    assert response_data['title'] == expected_title
    # print(response.headers)

@pytest.mark.skip
def test_get_all_names():
    response = requests.get(f'{base_url}users/')
    response_data = response.json()
    # print(response_data)
    name_list = []
    for i, name in enumerate(response_data):
        name_list.append((i+1, response_data[i]['name']))
    # print(name_list)
    return name_list

def get_all_names():
    response = requests.get(f'{base_url}users/')
    response_data = response.json()
    name_list = []
    for i, name in enumerate(response_data):
        name_list.append((i+1, response_data[i]['name']))
    return name_list

@pytest.mark.skip
@pytest.mark.parametrize('userId, expected_name', get_all_names())
def test_get_all_users_name(userId, expected_name):
    response = requests.get(f'{base_url}users/{userId}')
    response_data = response.json()
    assert response_data['name'] == expected_name, 'wrong name'

# второй сайт

def test_end_to_end():
    new_user = {
        'username': 'my user',
        'firstName': 'MyFirstname',
        'lastName': 'MyLastname',
        'email': str(time.time()) + '@example.com',
        'password': '12345'
    }

    response = requests.post(f'{url}user', data=new_user)
    assert response.status_code == 200

    response_data = response.json()
    assert 'id' in response_data.keys()
    user_id = response_data['id']

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == 200
    print('get==>', response.headers)
    # print(response.json())

    auth_data = {
        'email': new_user['email'],
        'password': '12345'
    }

    response = requests.post(f'{url}user/login', data=auth_data)
    assert response.status_code == HTTP_code, 'wrong status code'
    # print(response.headers)
    token = response.headers['x-csrf-token']
    auth_sid = response.cookies['auth_sid']
    # print(token, auth_sid)

    new_user_update = {
        'username': 'my user updater'
    }

    response = requests.put(f'{url}user/{user_id}',
                            data=new_user_update,
                            headers={'x-csrf-token': token},
                            cookies={'auth_sid':auth_sid})

    assert response.status_code == HTTP_code, 'wrong status code'

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == HTTP_code

    response_data = response.json()
    assert 'my user updater' in response_data.values()
    print('response_data==>', response_data)

    response = requests.delete(f'{url}user/{user_id}',
               headers={'x-csrf-token': token},
                cookies={'auth_sid': auth_sid})

    # print(response.headers)

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == 404