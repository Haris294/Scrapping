import json
import requests 
from datetime import datetime as dt 

def bitcoinprice():
    r = requests.get('https://www.bitstamp.net/api/ticker/bitcoin')
    json_r = json.loads(r.text)
    opening_rate = json_r['open']
    highest_rate = round(float(json_r['high']),2)
    lowest_rate = round(float(json_r['low']),2)
    latest_rate = json_r['last']
    updated_at = dt.fromtimestamp(int(json_r['timestamp']))
    
    print("\nOPENING RATE :     " + str(opening_rate))
    print("\nHIGHEST RATE :     " + str(highest_rate))
    print("\nLOWEST RATE :     " + str(lowest_rate))
    print("\nLATEST RATE :     " + str(latest_rate))
    print("\nUPDATED AT :     " + str(updated_at))



if __name__ == '__main__':
    bitcoinprice()
