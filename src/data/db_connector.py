from google.cloud import datastore
from google.cloud import storage
from itsdangerous import json
import logging
import os
import ndjson

bucket_client = storage.Client()

datastore_client = datastore.Client()

def store_question():
    questions_file = get_questions_file()

    for question in questions_file:
        entity = datastore.Entity(key=datastore_client.key('questions'))
        entity.update(question)
        datastore_client.put(entity)

def get_questions_file():

    bucket = bucket_client.get_bucket('tacer-bucker')
    blob = bucket.get_blob('questions.json')
    json_data_string = blob.download_as_string()

    json_data = ndjson.loads(json_data_string)
    return json_data

def fetch_question(number):
    query = datastore_client.query(kind='questions')
    question = list(query.add_filter("number", "=", number).fetch(limit=1))

    print("Question: " + str(number) + "recovered")
    return question[0] if len(question) > 0 else None

def get_total_elements():
    return len(list(datastore_client.query(kind='questions').fetch()))