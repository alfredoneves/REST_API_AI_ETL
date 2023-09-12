#!/usr/bin/python3

import json
import requests
import openai
import pandas as pd

# extract
df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()

base_url = 'https://sdw-2023-prd.up.railway.app/'
base_url2 = 'http://127.0.0.1:8000/'


def get_user(id):
	response = requests.get(f'{base_url2}/id={id}')
	return response.json() if response.status_code == 200 else None
	
# read chatgpt API key from file
my_file = open('../chatgpt.key', 'r')
openai.api_key = my_file.read().strip()
my_file.close()


def generate_response(user):
	completion = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[
		{
			"role": "system",
			"content": "You're a specialist in banking markting"
		},
		{
			"role": "user",
			"content": f"Write a message to {user['name']} about investment (maximun of 100 characters)"
		}
	]
	)
	
	return completion.choices[0].message.content.strip
	
	
# transform
def update_user(user):
	response = requests.put(f"{base_url2}/users}", json=user)
	return True if response.status_code == 200 else False


users = [user for id in user_ids if (user := get_user(id)) is not None]

# load
for user in users:
	news = generate_response(user)
	user['news'].append({"description": news})
	update_user(user)
	print(f"{user['name']} updated")
