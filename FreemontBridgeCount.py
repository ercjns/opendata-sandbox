# Eric Jones
# March 2015

# working from dev.socrata.com

# City of Seattle / Socrata Open Data endpoint:
# https://data.seattle.gov/resource/65db-xm6k.json
# Fields: date, freemont_bridge_nb, freemont_bridge_sb

# Other interesting data
# Elliott Bay Trail bikes and peds: https://data.seattle.gov/resource/4qej-qvrz.json

import requests
# import datetime
# import scipy


SoQL = {
            '$where': "date > '2015-01-01T00:00:01'",
            '$order': 'date ASC'
          }

r = requests.get('https://data.seattle.gov/resource/65db-xm6k.json', params=SoQL)

data = r.json()


for e in data:
    print e.keys(), e.values()
    # print (str(e.date), str(e.freemont_bridge_sb), str(e.freeomont_bridge_nb))
