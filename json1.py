import urllib
import json

u = urllib.urlopen("http://python-data.dr-chuck.net/comments_354917.json ")
data = u.read()
final = json.loads(data)
total = 0
for comment in final["comments"]:
    total = total + int(comment["count"])

print total
