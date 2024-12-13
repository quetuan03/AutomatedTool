# sql_injection_scanner.py
import requests
from colorama import Fore , Style
import time
def load_sql_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_sql_injection(url, params, sql_payloads,method='get'):
    vulnerable = False
    # print(params)
    # print("AAAA")
    cookies = {'session':'{Input cookie}'}
    for payload in sql_payloads:
        # test_params = {key: payload for key in params.keys()}
        test_params = {}
       
        for key,value in params.items():
            if key == "csrf":
                test_params['csrf'] = value
                continue
            test_params[key]=payload
        # print(test_params)
        response =""
        if method == "get" :
            response = requests.get(url, params=test_params,cookies=cookies)
        else :
            response = requests.post(url, data=test_params,cookies=cookies)

        if "Error" in response.text or  response.status_code >= 500:
            print(f"\nPossible SQL Injection vulnerability found with payload: {payload}")           
            vulnerable = True
    return vulnerable
