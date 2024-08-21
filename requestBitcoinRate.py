#------------------------------------------------------------------------#
#   File : requestBitcoinRate.py
#   Author : Ahmed ElSherif                                              #
#   Path : Repo/paython_scripts
#------------------------------------------------------------------------#

#pip install pprint (To make the json more readable)
#pip install requests

import requests
from pprint import pprint

api=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

pprint(api.json())