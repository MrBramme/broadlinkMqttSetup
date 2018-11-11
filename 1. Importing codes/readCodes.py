import os
import json

codes = []
for file in os.listdir("."):
    if file.endswith(".txt"):
        with open(file) as f:
            lines = f.read().splitlines()
            outputJson = {"file": file}
            for line in lines:
                    if line.startswith("Button Name:"):
                            outputJson["name"] = line[13:len(line)]
                            if len(line) > 13:
                                    outputJson["topic"] = file[0:len(file)-4].lower() + "/" + line[13:len(line)].lower()
                            else:
                                    outputJson["topic"] = "unknown"
                    elif line.startswith("Button ID:"):
                            outputJson["id"] = line[11:len(line)]
                    elif line.startswith("Code:"):
                            outputJson["code"] = line[6:len(line)]
                            codes.append(outputJson)
                            outputJson = {"file": file}

def saveOutput():
    with open('output.json', 'w') as outfile:
        json.dump(codes, outfile)
    print("output saved to output.json")

exists = os.path.isfile('output.json')
if exists:
    canOverwrite = raw_input("File output.json exists, can I overwrite (y/n): ")
    if canOverwrite.lower() == "y":
            saveOutput()
else:
    saveOutput()
