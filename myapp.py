import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"
# I am sending get requeste because i read student record from database table

# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     r = requests.get(url=URL, data=json_data)
#     data = r.json()
#     print(data)
# get_data()


def post_data():
    data = {
        'name': 'Misbah',
        'roll': 23,
        'city': 'kohat'
    }
    # convert this dictinory data into json data
    json_data = json.dumps(data)
    # send request 
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    # response print
    print(data)
post_data()


# implementing updating data

def update_data():
    data = {
        'id':2,
        'name':'HELLO',
        'city': 'BOKARO',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()
    
def delete_data():
    data = {
        'id':3
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# delete_data()

