#!/usr/bin/python3

import json
from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()	# instances the class

users = [{
  "id": 0,
  "name": "Devweekerson",
  "account": {
    "id": 1,
    "number": "01.097954-4",
    "agency": "2030",
    "balance": 624.12,
    "limit": 1000
  },
  "card": {
    "id": 1,
    "number": "xxxx xxxx xxxx 1111",
    "limit": 2000
  },
},
{
  "id": 1,
  "name": "Bruce",
  "account": {
    "id": 2,
    "number": "01.097954-5",
    "agency": "2030",
    "balance": 10000.00,
    "limit": 500
  },
  "card": {
    "id": 2,
    "number": "xxxx xxxx xxxx 2222",
    "limit": 500
  },
},
{
  "id": 2,
  "name": "Clark",
  "account": {
    "id": 3,
    "number": "01.097954-6",
    "agency": "2030",
    "balance": 1000.00,
    "limit": 200
  },
  "card": {
    "id": 3,
    "number": "xxxx xxxx xxxx 3333",
    "limit": 300
  },
}
]

all_users = []
    
    
@app.get("/id={id}")	# works when the root directory in the site is requested with a get
def root(id: int):
	if id >= 0 and id < len(users):
		return users[id]
	else:
		return 'User not found'
	
	
@app.get("/users")
def get_users():
	return all_users


@app.put("/users")
def create_user(data: Dict[Any, Any]):
	global all_users
	all_users.append(data)
