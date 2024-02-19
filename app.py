from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def extract_content():
    url = "https://erp.webkul.com/application/status/DIVYH5KOW012024"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    target_element = soup.find(class_='col-md-8 col-md-offset-2 col-xs-12 mt8')
    application_status = target_element.find('strong', text='Application Status :').find_next('span').text.strip()
    print(application_status)
    return application_status

    