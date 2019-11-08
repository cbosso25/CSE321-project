import requests
import json
from datetime import datetime
from satellites import passes

sat_id = '25338'
observer_lat = '43.033'
observer_long = '-78.704'
observer_alt = '0'
days = '2'
min_elevation = '20'
passes(sat_id,observer_lat,observer_long,observer_alt,days,min_elevation)

sat_id = '33591'
observer_lat = '43.033'
observer_long = '-78.704'
observer_alt = '0'
days = '2'
min_elevation = '20'
passes(sat_id,observer_lat,observer_long,observer_alt,days,min_elevation)