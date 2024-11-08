#!/home/elcot/Personal/problem1/venv/bin/python3
import sys
import os
from dotenv import load_dotenv
from check_vt import runVirusTotal
from script import clamavStuff
from datetime import datetime


# loading configuration
load_dotenv('config.env')

# Virus Total API_KEY
API_KEY = os.getenv('API_KEY')

# Global Variables
# ANSI escape code for red text
RED = "\033[31m"
RESET = "\033[0m"  # Reset to default color

def createLogFile():
    # creating a log file for future reference or debugging
    log_file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_path = "logs/"+log_file_name+".txt"
    # creating log files for data storage
    f = open(log_path, "w")
    f.close()
    
    
def main():
    if(len(sys.argv) != 2):
        print("No file path given\n")
        print("Note: \n     Usage: python main.py <FILEPATH>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    # first we will perform virustotal API stuff...
    print("\n")
    print("Starting Checking: \n")
    print("Running Virustotal database occurence")
    
    virustotalResponse = runVirusTotal(file_path, API_KEY)
    
    if(virustotalResponse == True):
        print(f"{RED}Found Reference In VirusTotal Database for file: {file_path} {RESET}")
    else:
        print("No Reference found in VirusTotal Database for file: ", file_path)

    print("Done virustotal stuff....")
    
    # now running clamav CLI tool
    print("Analyze using ClamAv: ")
    
    clamavResponse = clamavStuff(file_path)
    
    if(clamavResponse == False):
        print("No infected files found ")
    else:
        print(f"{RED}Found Infected Files{RESET}")

    print("Finished Running Clamav")
        

if __name__ == "__main__":
    main()
