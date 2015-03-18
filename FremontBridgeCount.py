# Eric Jones
# March 2015

# working from dev.socrata.com
# working from plot.ly/python/user-guide

# City of Seattle / Socrata Open Data endpoint:
# https://data.seattle.gov/resource/65db-xm6k.json
# Fields: date, fremont_bridge_nb, fremont_bridge_sb

# Other interesting data
# Elliott Bay Trail bikes and peds: https://data.seattle.gov/resource/4qej-qvrz.json


##
# Big Goal number 1:
# Take a week's worth of data, and show it in a web browser:
    # A web-enabled line graph (x: time, y: volume) with interactive (hover) data points
    # An animation (?)
    # A text summary of the data


import json
import requests

from bottle import template

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as gobs



def getConfigValue(identifier):
    '''returns the key matching the identifier'''
    config = json.load(open('od-sandbox.config', 'r'))
    namespace, key = identifier.split('.', 1)
    return config[namespace][key]




def getFremontBridgeData(SoQL=None):
    url = 'https://data.seattle.gov/resource/65db-xm6k.json'
    # uncomment the next two lines to hit the server and get new data
    r = requests.get(url, params=SoQL)
    data = r.json()
    # uncomment the next line to use fake data rather than hitting the server
    # data = [{u'date': u'2015-01-30T01:00:00', u'fremont_bridge_nb': u'3', u'fremont_bridge_sb': u'7'}, {u'date': u'2015-01-30T02:00:00', u'fremont_bridge_nb': u'4', u'fremont_bridge_sb': u'6'}, {u'date': u'2015-01-30T03:00:00', u'fremont_bridge_nb': u'1', u'fremont_bridge_sb': u'2'}, {u'date': u'2015-01-30T04:00:00', u'fremont_bridge_nb': u'3', u'fremont_bridge_sb': u'1'}, {u'date': u'2015-01-30T05:00:00', u'fremont_bridge_nb': u'7', u'fremont_bridge_sb': u'19'}, {u'date': u'2015-01-30T06:00:00', u'fremont_bridge_nb': u'27', u'fremont_bridge_sb': u'59'}, {u'date': u'2015-01-30T07:00:00', u'fremont_bridge_nb': u'59', u'fremont_bridge_sb': u'179'}, {u'date': u'2015-01-30T08:00:00', u'fremont_bridge_nb': u'85', u'fremont_bridge_sb': u'254'}, {u'date': u'2015-01-30T09:00:00', u'fremont_bridge_nb': u'84', u'fremont_bridge_sb': u'133'}, {u'date': u'2015-01-30T10:00:00', u'fremont_bridge_nb': u'31', u'fremont_bridge_sb': u'59'}, {u'date': u'2015-01-30T11:00:00', u'fremont_bridge_nb': u'19', u'fremont_bridge_sb': u'47'}, {u'date': u'2015-01-30T12:00:00', u'fremont_bridge_nb': u'33', u'fremont_bridge_sb': u'47'}, {u'date': u'2015-01-30T13:00:00', u'fremont_bridge_nb': u'40', u'fremont_bridge_sb': u'43'}, {u'date': u'2015-01-30T14:00:00', u'fremont_bridge_nb': u'57', u'fremont_bridge_sb': u'55'}, {u'date': u'2015-01-30T15:00:00', u'fremont_bridge_nb': u'83', u'fremont_bridge_sb': u'72'}, {u'date': u'2015-01-30T16:00:00', u'fremont_bridge_nb': u'148', u'fremont_bridge_sb': u'97'}, {u'date': u'2015-01-30T17:00:00', u'fremont_bridge_nb': u'240', u'fremont_bridge_sb': u'102'}, {u'date': u'2015-01-30T18:00:00', u'fremont_bridge_nb': u'196', u'fremont_bridge_sb': u'91'}, {u'date': u'2015-01-30T19:00:00', u'fremont_bridge_nb': u'55', u'fremont_bridge_sb': u'32'}, {u'date': u'2015-01-30T20:00:00',u'fremont_bridge_nb': u'29', u'fremont_bridge_sb': u'18'}, {u'date': u'2015-01-30T21:00:00', u'fremont_bridge_nb': u'18', u'fremont_bridge_sb': u'12'}, {u'date': u'2015-01-30T22:00:00', u'fremont_bridge_nb': u'11', u'fremont_bridge_sb': u'11'}, {u'date': u'2015-01-30T23:00:00', u'fremont_bridge_nb': u'9', u'fremont_bridge_sb': u'13'}, {u'date': u'2015-01-31T00:00:00', u'fremont_bridge_nb': u'9', u'fremont_bridge_sb': u'8'}, {u'date': u'2015-01-31T01:00:00', u'fremont_bridge_nb': u'1', u'fremont_bridge_sb': u'2'}, {u'date': u'2015-01-31T02:00:00', u'fremont_bridge_nb': u'2', u'fremont_bridge_sb': u'2'}, {u'date': u'2015-01-31T03:00:00', u'fremont_bridge_nb': u'0', u'fremont_bridge_sb': u'2'}, {u'date': u'2015-01-31T04:00:00', u'fremont_bridge_nb': u'1', u'fremont_bridge_sb': u'2'}, {u'date': u'2015-01-31T05:00:00', u'fremont_bridge_nb': u'2', u'fremont_bridge_sb': u'0'}, {u'date': u'2015-01-31T06:00:00', u'fremont_bridge_nb': u'10', u'fremont_bridge_sb': u'5'}, {u'date': u'2015-01-31T07:00:00', u'fremont_bridge_nb': u'8', u'fremont_bridge_sb': u'11'}, {u'date': u'2015-01-31T08:00:00', u'fremont_bridge_nb': u'19', u'fremont_bridge_sb': u'28'}, {u'date': u'2015-01-31T09:00:00', u'fremont_bridge_nb': u'38', u'fremont_bridge_sb': u'46'}, {u'date': u'2015-01-31T10:00:00', u'fremont_bridge_nb': u'28', u'fremont_bridge_sb': u'44'}, {u'date': u'2015-01-31T11:00:00', u'fremont_bridge_nb': u'35', u'fremont_bridge_sb': u'46'}, {u'date': u'2015-01-31T12:00:00', u'fremont_bridge_nb': u'48', u'fremont_bridge_sb': u'65'}, {u'date': u'2015-01-31T13:00:00', u'fremont_bridge_nb': u'67', u'fremont_bridge_sb': u'81'}, {u'date': u'2015-01-31T14:00:00', u'fremont_bridge_nb': u'66', u'fremont_bridge_sb': u'69'}, {u'date': u'2015-01-31T15:00:00', u'fremont_bridge_nb': u'58', u'fremont_bridge_sb': u'68'}, {u'date': u'2015-01-31T16:00:00', u'fremont_bridge_nb': u'61', u'fremont_bridge_sb': u'76'}, {u'date': u'2015-01-31T17:00:00', u'fremont_bridge_nb': u'42', u'fremont_bridge_sb': u'39'}, {u'date': u'2015-01-31T18:00:00', u'fremont_bridge_nb': u'20', u'fremont_bridge_sb': u'26'}, {u'date': u'2015-01-31T19:00:00', u'fremont_bridge_nb': u'8', u'fremont_bridge_sb': u'10'}, {u'date': u'2015-01-31T20:00:00', u'fremont_bridge_nb': u'17', u'fremont_bridge_sb': u'8'}, {u'date': u'2015-01-31T21:00:00', u'fremont_bridge_nb': u'13', u'fremont_bridge_sb': u'8'}, {u'date': u'2015-01-31T22:00:00',u'fremont_bridge_nb': u'14', u'fremont_bridge_sb': u'6'}, {u'date': u'2015-01-31T23:00:00', u'fremont_bridge_nb': u'6',u'fremont_bridge_sb': u'11'}]
    return data

def plotFremontBridgeData(unzipped):
    dates = unzipped[0]
    nb = unzipped[1]
    sb = unzipped[2]
    # dates = []
    # nb = []
    # sb = []
    # for e in SODA:
    #     dates.append(e['date'].replace('T', ' '))
    #     nb.append(int(e['fremont_bridge_nb']))
    #     sb.append(int(e['fremont_bridge_sb']))


    py.sign_in(getConfigValue('plotly.user'), getConfigValue('plotly.key'))

    trace1 = gobs.Scatter(
        x=dates,
        y=sb,
        mode='lines+markers',
        name='South-bound'
    )
    trace2 = gobs.Scatter(
        x=dates,
        y=nb,
        mode='lines+markers',
        name='North-bound'
    )

    data = gobs.Data([trace1, trace2])
    layout = gobs.Layout(
        title = 'Fremont Bridge Bike Traffic',
        xaxis1 = gobs.XAxis(title='time', showgrid=False),
        yaxis1 = gobs.YAxis(title='bicycles')
    )
    fig = gobs.Figure(data=data, layout=layout)

    plot_url = py.plot(fig, filename='FremontBridge', auto_open=False)
    return plot_url

def drawFremontBridgeAnimate(unzipped):
    dates = unzipped[0]
    nb = unzipped[1]
    sb = unzipped[2]
    print 'hello!'

    #set up the key frames
    keys = [a*100/(len(dates)-1) for a in range(len(dates)-1)]
    keys.append(100)
    keys = [str(a)+'%' for a in keys]
    frames = [a+' '+'{width: '+str(b)+'px;}' for (a,b) in zip(keys,nb)]

    style = '.ani1{width:100px; height:100px; background:#F81; -webkit-animation: mymove 10s infinite; animation: mymove 10s infinite;}'

    # save the keyframe css
    webkitani = "@-webkit-keyframes mymove {" + ''.join(frames) + "}"
    standardani = "@keyframes mymove {" + ''.join(frames) +  "}"

    div = "<div class=ani1></div>"

    anihtml = '<style>' + style + webkitani + standardani + '</style>\n' + div
    return anihtml


def unzipFremontSODA(SODA):
    dates = []
    nb = []
    sb = []
    for e in SODA:
        dates.append(e['date'].replace('T', ' '))
        nb.append(int(e['fremont_bridge_nb']))
        sb.append(int(e['fremont_bridge_sb']))
    return (dates, nb, sb)

def getFremontBridge():
    query = {'$where': "date > '2015-01-07T00:00:00' AND date < '2015-01-10T23:59:59'",
             '$order': "date ASC"}
    soda = getFremontBridgeData(query)
    unzipped = unzipFremontSODA(soda)
    ploturl = plotFremontBridgeData(unzipped)
    animate = drawFremontBridgeAnimate(unzipped)
    r = requests.get(ploturl+'.html')
    plothtml = r.text

    return template('basetemplate',
                    plothtml=plothtml,
                    animatehtml=animate
                    )

if __name__ == '__main__':
    print "hello"
    query=None
    soda = getFremontBridgeData(query)
    unzipped = unzipFremontSODA(soda)
    animate = drawFremontBridgeAnimate(unzipped)
