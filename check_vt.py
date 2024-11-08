import requests
import sys
import json
import os
import subprocess
from dotenv import load_dotenv

# global variables
BASE_URL = 'https://www.virustotal.com/api/v3/files/'

# this will give request to totalVirus website
def check_hash(hash_value, API_KEY):
    headers = {
        'accept': 'application/json',
        'x-apikey': API_KEY
    }
    response = requests.get(BASE_URL + hash_value, headers=headers)
    # if our code finds a reference to one of the database sha256sum then it alerts us.
    # make a file json request filled with requests and stuff...
    with open("logs/jsonData.json", "w") as jsonF:
        json.dump(response.json(), jsonF, indent=4)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


# def check_file(file_path, API_KEY):
#     with open(file_path) as f:
#         files = {'files': (file_path,f)}
#         response = requests.post(BASE_URL, headers={'x-apikey': API_KEY}, files=files)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None


def runVirusTotal(FILE_PATH, API_KEY):
    file_path = FILE_PATH
    command = ['sha256sum', file_path]
    
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout.split(' ')
    hash_value = result[0]
    
    print("File Name: ", FILE_PATH, "Hash: ", hash_value)
    
    hashValueresult = check_hash(hash_value, API_KEY)
    if hashValueresult:
        return True
    else:
        return False

