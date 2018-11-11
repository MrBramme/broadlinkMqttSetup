import os
import json

with open('output.json') as f:
    jsonData = json.load(f)

for data in jsonData:
    path = data["topic"].rsplit('/', 1)[0].replace('broadlink/', 'commands/')
    fileName = data["topic"].replace('broadlink/', 'commands/')
    if not os.path.exists(path):
        os.makedirs(path)
    with open(fileName, 'wb') as f:
        f.write(data["code"])
    
print("Done creating the commands!")