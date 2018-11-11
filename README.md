# broadlinkMqttSetup
A tutorial on how to setup broadlink mqtt for use with Home-Assistant

Current state: **work in progress**

# Dependencies
We'll be using MQTT as our backbone. So you'll need an MQTT broker, and this will be the client that'll bridge MQTT to our Broadlink device: [Broadlink-mqtt](https://github.com/eschava/broadlink-mqtt)

# Step 1: Getting the codes
As noted on the [Broadlink page on HA docs](https://www.home-assistant.io/components/switch.broadlink/), you can export the codes from your e-remote app. This is by far the easiest way of doing it in bulk.  
Another way is finding a list of codes like [this](https://github.com/yahat/broadlink_mini_homeassistant_ir_codes_samsung_tv), but you won't find this for all your devices.

# Step 2: Import those codes into Broadlink-mqtt (rather than learning them one by one)
Start by cloning this repo locally
```
git clone https://github.com/MrBramme/broadlinkMqttSetup.git
```

Drop the exported codes from Step 1 in the folder `1. Importing codes`. You'll notice mine in there. Next run the python code to create a json file of your codes:
```
cd 1.\ Importing\ codes/
python readCodes.py
```
This will create a json file named output.json with the codes from the text files. In that json file you'll see a suggested topic based on the filename & button name from your e-remote app. If no name found, it'll put "unknown" there.

The next step is to check those topics. So open up the output.json and check them, don't link them? Simply adjust them :)

Next up is to import them in the commands folder of our broadlink-mqtt client. This, of course, has to happen on the actual device that'll run that client, or run it on your current device and copy the commands folder to the client-device.

so: place your output.json file in the same folder as the script found in `2. Create commands`. and then smply run:
```
python createCommands.py
```

... To continue here ...


# Links

- [Samsung tv codes](https://github.com/yahat/broadlink_mini_homeassistant_ir_codes_samsung_tv)
- [Base64 to hex converter](https://cryptii.com/pipes/base64-to-hex)