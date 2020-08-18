import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com','youtube.com','amazon.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    #seconds = random.randrange()