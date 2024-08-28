import json



from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class UserResponse(BaseModel):
    data: User
    support: Support


class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
    support: Support

HOST = '127.0.0.1'

user_json = [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    {
      "id": 2,
      "email": "janet.weaver@reqres.in",
      "first_name": "Janet",
      "last_name": "Weaver",
      "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    {
      "id": 3,
      "email": "emma.wong@reqres.in",
      "first_name": "Emma",
      "last_name": "Wong",
      "avatar": "https://reqres.in/img/faces/3-image.jpg"
    },
    {
      "id": 4,
      "email": "eve.holt@reqres.in",
      "first_name": "Eve",
      "last_name": "Holt",
      "avatar": "https://reqres.in/img/faces/4-image.jpg"
    },
    {
      "id": 5,
      "email": "charles.morris@reqres.in",
      "first_name": "Charles",
      "last_name": "Morris",
      "avatar": "https://reqres.in/img/faces/5-image.jpg"
    },
    {
      "id": 6,
      "email": "tracey.ramos@reqres.in",
      "first_name": "Tracey",
      "last_name": "Ramos",
      "avatar": "https://reqres.in/img/faces/6-image.jpg"
    }
  ]


def get_data():
    # with open('mservice/data/users.json') as data_file:
        users = {}
        data = user_json
        for row in data:
            users[row["id"]] = User(id=row["id"], email=row["email"], first_name=row["first_name"],
                                    last_name=row["last_name"], avatar=row["avatar"])
        support_data = Support(url=f"http://{HOST}/#support-heading",
                               text=f"Some text message from support")
        return users, support_data


users, support_info = get_data()

if users.get(10):
    print('ok')