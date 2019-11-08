# CSE321-project
NOAA Weather Satellite Receiver

radio.py is a simple FM demodulator that uses GNU Radio and an RTL-SDR to listen to FM broadcasts

satellites.py defines a function passes that queries N2YO.com API to gather data on satellite pass times for the NOAA 15, 18, and 19

satellites_test.py is a test script which uses the passes functions to generate pass data for the next 2 days for Buffalo, NY for the satellites NOAA 15 and NOAA 19
