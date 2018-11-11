import os
import json

print("Please select a mode:")
print("  1. Only create the command folder(s)")
print("  2. Only create HA config")
print("  3. Create command folder(s) and HA config")
mode = raw_input("Choose mode (1/2/3): ")

with open('output.json') as f:
    jsonData = json.load(f)

if mode == "1" or mode == "3":
    for data in jsonData:
        path = data["topic"].rsplit('/', 1)[0].replace('broadlink/', 'commands/')
        fileName = data["topic"].replace('broadlink/', 'commands/')
        if not os.path.exists(path):
            os.makedirs(path)
        with open(fileName, 'wb') as f:
            f.write(data["code"])
    print("Done creating the commands!")

if mode == "2" or mode == "3":
    HaConfig = []
    for data in jsonData:
        HaConfig.append('- platform: mqtt')
        HaConfig.append('  name: "' + data['name'] + '"')
        HaConfig.append('  command_topic: "' + data['topic'] + '"')
        HaConfig.append('  payload_on: "replay"')
        HaConfig.append('  payload_off: "replay"')
    with open("HaConfig.yaml", 'wb') as f:
        f.write("\n".join(HaConfig))
    print("Done creating the HA Config!")
