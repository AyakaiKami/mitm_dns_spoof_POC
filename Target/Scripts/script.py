#!/usr/bin/python3

import requests
import datetime
import warnings

url="https://www.google.com/"
warnings.filterwarnings("ignore")
response=requests=requests.get(url=url,verify=False)

if response.text=="Message: You got tricked!":
    print("Got tricked:(")
else:
    print("Secure")
exit(0)
