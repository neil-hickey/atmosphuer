import json
import os

def write_sample_json_file():
    print("writing json samples")
    #{"name": "rain", "brightness": "254", "hue": "15000", "saturation": "120", "audio": "rain.mp3" }
    json_scenes = {
        "name": "rain",
        "brightness": "254",
        "hue": "15000",
        "saturation": "120",
        "audio": "rain.mp3",
    }

    #{"bridge_ip": "192.168.0.10", "shadowrun_lights": "Arbeitszimmer"}
    json_settings = {
        "bridge_ip": "192.168.0.10",
        "shadowrun_lights": "Arbeitszimmer",
    }

    #write to file
    f = open("scenes.json","w")
    f.write(json.dumps(json_scenes))
    f.close()

    f = open("settings.json","w")
    f.write(json.dumps(json_settings))
    f.close()

    print("files written")

def load_settings():
    settings = os.getcwd()+"/settings.json"
    return load(settings)

def load_scenes():
    scenes = os.getcwd()+"/scenes.json"
    return load(scenes)

def load(filename):
    if os.path.exists(filename):
        print("Loading "+filename)
        file = open(filename,"r")
        content = file.read()
        file.close()
        return json.loads(content)
    else:
        print ("Could not find file "+filename)
        print ("Exiting")