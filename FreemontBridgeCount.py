# Eric Jones
# March 2015

# working from dev.socrata.com

# City of Seattle / Socrata Open Data endpoint:
# https://data.seattle.gov/resource/65db-xm6k.json
# Fields: date, freemont_bridge_nb, freemont_bridge_sb

# Other interesting data
# Elliott Bay Trail bikes and peds: https://data.seattle.gov/resource/4qej-qvrz.json


##
# Big Goal number 1:
# Take a week's worth of data, and show it in a web browser:
    # A web-enabled line graph (x: time, y: volume) with interactive (hover) data points
    # An animation (?)
    # A text summary of the data


import requests


def getFreemontBridgeData(SoQL=None):
    url = 'https://data.seattle.gov/resource/65db-xm6k.json'
    r = requests.get(url, params=SoQL)
    data = r.json()
    print type(data)
    return
    # for e in data:
    #     print e.keys(), e.values()
    #     # print (str(e.date), str(e.freemont_bridge_sb), str(e.freeomont_bridge_nb))
