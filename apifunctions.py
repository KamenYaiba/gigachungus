import json
import string
import random


def generate_rep_id(chat_id):
    with open('rep_ids.json', 'r') as file:
        ids = json.load(file)
    rep_id = random_string()
    ids[rep_id] = chat_id
    with open('rep_ids.json', 'w') as file:
        json.dump(ids, file)
    return rep_id


def get_chat_id(rep_id):
    with open('rep_ids.json', 'r') as file:
        ids = json.load(file)
    id = ids[rep_id]
    if id is None:
        return -1
    destroy_rep_id(rep_id)
    return id


def destroy_rep_id(rep_id):
    with open('rep_ids.json', 'r') as file:
        ids = json.load(file)
    del ids[rep_id]
    with open('rep_ids.json', 'w') as file:
        json.dump(ids, file)
    return 'destroyed'


def random_string():
    chars = string.ascii_letters + string.digits
    ranstr = ""
    for i in range(8):
        ranstr = ranstr + random.choice(chars)
    return ranstr