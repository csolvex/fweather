import requests, urllib, json, os
import subprocess
import platform, maya

def screen_clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)


f = urllib.request.urlopen('http://api.wunderground.com/api/35d26346bc2bfe43/geolookup/conditions/q/MI/detroit.json')
#f = urllib.request.urlopen('http://api.wunderground.com/api/35d26346bc2bfe43/geolookup/conditions/Canada/Ontario/windsor.json')

json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
temp_c = parsed_json['current_observation']['temp_c']
RH = parsed_json['current_observation']['relative_humidity']
weather = parsed_json['current_observation']['weather']
last_obs = parsed_json['current_observation']['observation_time']

# clear screen and display parsed data
# screen_clear()
print ("Current temperature in %s is: %s F, %s C" % (location, temp_f, temp_c))
print ("The weather is: %s " % (weather))
print ("Relative Humidity: %s" % (RH))
print (last_obs)


f.close()
