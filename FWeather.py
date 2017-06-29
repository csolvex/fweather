# same as original app but I added color to the output, all window dressing.

import requests, urllib, json, os, subprocess, platform, maya
from termcolor import colored
from platform import system as system_name
from os import system as system_call

def clear_screen():
    command = "-cls" if system_name().lower()=="windows" else "clear"
    system_call(command)

# Clear the terminal
clear_screen()

# Connect with API
f = urllib.request.urlopen('http://api.wunderground.com/api/35d26346bc2bfe43/geolookup/conditions/q/MI/detroit.json')
#f = urllib.request.urlopen('http://api.wunderground.com/api/35d26346bc2bfe43/geolookup/conditions/Canada/Ontario/windsor.json')

DTnow = maya.now()
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
temp_c = parsed_json['current_observation']['temp_c']
RH = parsed_json['current_observation']['relative_humidity']
weather = parsed_json['current_observation']['weather']
last_obs = parsed_json['current_observation']['observation_time']
Last_ob = colored(last_obs, 'red')

print (colored(" "*50, 'cyan', attrs=['underline']))
print (colored("Current temperature in %s is: %s F, %s C" ,"yellow") % (location, temp_f, temp_c))
print ("The weather is: %s " % (weather))
print ("Relative Humidity: %s" % (RH))
#print (last_obs)
print (Last_ob)

f.close()
