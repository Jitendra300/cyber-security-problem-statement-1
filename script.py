import sys
import subprocess

# ANSI escape code for red text
RED = "\033[31m"
RESET = "\033[0m"  # Reset to default color


def clamavStuff(FILE_PATH):
    file_path = FILE_PATH
    command = ['clamscan', '-r', file_path]
    
    result = subprocess.run(command, capture_output=True, text=True)
    # print(result.stdout)
    result_lines = result.stdout.split('\n')

    # now we also want to save the output lines to one log file...
    with open("logs/clamavLog.txt", "w") as clamavF:
        for i in result_lines:
            clamavF.write(i+'\n')

    print("Important Info: ")
    print(result_lines[5])
    print(result_lines[6])
    print(result_lines[7])
    
    print("\n")
    
    print("Runtime of Clamav: ")
    print(result_lines[-3])
    print(result_lines[-2])
    print(result_lines[-1])

    num_infected_files = result_lines[5].split(' ')[-1]
    print('\n')
    
    if(num_infected_files != '0'):
        return num_infected_files

    print("Full info:")
    print(result.stdout)

    return False

