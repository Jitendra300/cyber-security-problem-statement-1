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


def runVirusTotal(FILE_PATH, API_KEY):
    file_path = FILE_PATH
    # equivalent of running sha256sum file_path in terminal...
    command = ['sha256sum', file_path]
    
    result = subprocess.run(command, capture_output=True, text=True)
    # get output of the command with spliting of a whitespace
    result = result.stdout.split(' ')
    hash_value = result[0]
    
    print("File Name: ", FILE_PATH, "Hash: ", hash_value)

    # requests the totalvirus website for info of the given HASHVALUE
    hashValueresult = check_hash(hash_value, API_KEY)
    if hashValueresult:
        return True
    else:
        return False

