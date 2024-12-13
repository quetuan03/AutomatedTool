# utils.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
def extract_forms(url):
    cookies = {'session':'{Input cookie}'}
    response = requests.get(url,cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    
    forms = soup.find_all("form")
    form_details = []
    
    for form in forms:
        action = form.attrs.get("action")
        method = form.attrs.get("method", "get").lower()
        form_action = urljoin(url, action)
        
        inputs = []
        for input_tag in form.find_all("input"):
            input_name = input_tag.attrs.get("name")
            input_type = input_tag.attrs.get("type", "text") 
            input_value = input_tag.attrs.get("value", "")
            inputs.append({"name": input_name, "type": input_type, "value": input_value})
        
      
        form_details.append({
            "action": form_action,
            "method": method,
            "inputs": inputs
        })
    
    return form_details

def submit_form(form, url, payload):
    
    action = form.get("action")
    post_url = urljoin(url, action)
    inputs = form.get("inputs")
    data = {input.get("name"): payload for input in inputs if input.get("name")}
    
    print(f"Submitting to {post_url} with data: {data}")
    
    if form.get("method") == "post":
        return requests.post(post_url, data=data)
    else:
        return requests.get(post_url, params=data)
