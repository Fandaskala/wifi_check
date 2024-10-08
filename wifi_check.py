from json import dump, load
from time import strftime, localtime, sleep
from colorama import Fore
import requests
print ('wifi connection tester started\n you can find log.json for successful connection\n process started: \n\n\n')
def file_write_log(str: str) -> None:
    timer = strftime("%Y-%m-%d %H:%M:%S", localtime())
    try:
        with open('log.json', "r", newline=None) as log_read:
            data = load(log_read)
        with open('log.json', 'w') as js_write:
            dump(data + timer + str +"   ", js_write)
    except(FileNotFoundError):
        with open('log.json', 'w') as js_write:
            dump(timer + str, js_write)       
while True:
    timer = strftime("%Y-%m-%d %H:%M:%S", localtime())
    try:
        # Replace "https://www.google.com/" with a preferred website
        response = requests.get("https://www.google.com/", timeout=5)  # Set a timeout
        response.raise_for_status()  # Raise exception for non-2xx status codes
        print(timer, Fore.GREEN, " connected to wifi", Fore.WHITE)
        file_write_log(" connected to wifi")
        sleep(15)  # Wait 15 seconds before checking again
    except (requests.exceptions.RequestException, TimeoutError):
        print(timer ,Fore.RED ," Timeout conection failed", Fore.WHITE)