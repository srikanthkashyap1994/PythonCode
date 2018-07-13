import urllib
import json
serviceurl = "http://python-data.dr-chuck.net/geojson?"
while True:
    address = raw_input("Enter the address: ")
    url = serviceurl + urllib.urlencode({'sensor':'false','address':address})
    if (len(address) < 1):
        break
    uh = urllib.urlopen(url)
    text = uh.read()
    try:
        data = json.loads(text)
    except:
        data = None
    if 'status' not in data or data['status'] != 'OK':
        print '===Failure to retrieve data==='
        #print text
        continue
    print data["results"][0]["place_id"]
