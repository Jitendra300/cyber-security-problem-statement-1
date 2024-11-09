#!/home/elcot/Personal/problem1/venv/bin/python3
import sys
import argparse
import os
from dotenv import load_dotenv # this module is for protecting our API
from check_vt import runVirusTotal
from script import clamavStuff
from datetime import datetime


# loading configuration
load_dotenv('config.env')

# Virus Total API_KEY
API_KEY = os.getenv('API_KEY')

# Global Variables
# ANSI escape code for red text
RED = "\033[31m" # READ ESCAPE COLOR
RESET = "\033[0m"  # Reset to default color


# Creating the parser
parser = argparse.ArgumentParser(description='Malware Analysis Program')
# Add arguments
parser.add_argument('--file', type=str, required=True, help='The path to the file to process.')
parser.add_argument('--network_status', type=str, choices=['yes', 'no'], default='no', help='Network status (yes or no).')
# Parse the arguments
args = parser.parse_args()


def createLogFile():
    # creating timestamp of log files...that is changing name....one from json and another form clamavLog...
    log_file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    full_log_path = "logs/"+log_file_name

    # if network is on then only change name of the json file
    if(args.network_status != 'no'):
        old_json_name = "logs/jsonData.json"
        new_json_name = full_log_path+".json"
        os.rename(old_json_name, new_json_name)

    # changing name of clamavlog.txt to timestamp.txt
    old_clamav_name = "logs/clamavLog.txt"
    new_clamav_name = full_log_path+".txt"
    os.rename(old_clamav_name, new_clamav_name)
    
def main():
    # getting values from command arguments
    file_path = args.file
    network_flag = args.network_status
    
    print("\n")
    print("Starting Checking: \n")
    
    # if network is on then first we will perform virustotal API stuff...
    if(network_flag != 'no'):
        print("Running Virustotal database occurence")
        virustotalResponse = runVirusTotal(file_path, API_KEY)
        if(virustotalResponse == True):
            print("Found Reference In VirusTotal Database for file: ", file_path)
        else:
            print("No Reference found in VirusTotal Database for file: ", file_path)
        print("Done virustotal stuff....")
    else:
        print("Network Restriction given thus not using virustotal API.\n")
    
    # now running clamav CLI tool
    print("Analyze using ClamAv: ")
    clamavResponse = clamavStuff(file_path)
    if(clamavResponse == False):
        print("No infected files found ")
    else:
        print("Found Infected Files")
    print("Finished Running Clamav")

    print("\n")
    # logs are saved in /logs for future reference and debugging stuff....
    print("Saving Log Files for Future Reference.")
    createLogFile()
    print("\n")
    print("Done creating Log files")
        

if __name__ == "__main__":
    main()
