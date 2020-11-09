import requests
from requests.structures import CaseInsensitiveDict
import sys
import json

key_file = open('keys.txt', 'r')
keys = key_file.read().splitlines()
api_key = keys[0]
api_key_secret = keys[1]
bearer_token = keys[2]
user = sys.argv[1]


def get_user_ids(_user):
    # Code generate here: https://reqbin.com/req/c-w7oitglz/convert-curl-to-http-request
    # That website is incredible!!!
    url = "https://api.twitter.com/1.1/friends/ids.json?screen_name=" + _user
    headers = CaseInsensitiveDict()
    headers["authorization"] = "Bearer " + bearer_token
    resp = requests.get(url, headers=headers)
    json_list = json.loads(resp.text)
    _user_ids = json_list['ids']
    return _user_ids


def create_list():
    url = 'https://api.twitter.com/1.1/lists/create.json'
    headers = CaseInsensitiveDict()
    headers['name'] = 'test_01'
    headers['mode'] = 'private'
    resp = requests.post(url, headers=headers)

    return 'list_id'


user_ids = get_user_ids(user)

# Authenticate user
# https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens


# Create list
# https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create
create_list()

# Add to list
# 100 per API call
# https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create_all


hi = 0