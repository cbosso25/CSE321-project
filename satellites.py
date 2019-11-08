import requests
import json
from datetime import datetime

def passes(sat_id,observer_lat,observer_long,observer_alt,days,min_elevation):
    url0 = 'https://www.n2yo.com/rest/v1/satellite/radiopasses/{}/{}/{}/{}/{}/{}/&apiKey=JQW9TD-RYU96K-8DX2QW-484S'
    url = url0.format(sat_id,observer_lat,observer_long,observer_alt,days,min_elevation)
    s = requests.get(url).text
    satellites = json.loads(s)

    print(satellites['info']['satname'] + ' Passes in next 2 days (UTC Time):\n')
    for sat_pass in satellites['passes']:
        dt = datetime.utcfromtimestamp(sat_pass['startUTC'])
        #print(dt)
        if dt.hour > 12:
            print(str(dt.month)+'/'+str(dt.day),str(dt.hour-12)+':'+str(dt.minute)+ ' PM\n')
        else:
            print(str(dt.month)+'/'+str(dt.day),str(dt.hour)+':'+str(dt.minute)+ ' AM\n')
