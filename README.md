# Smart Room Manager

This was a project I created as part of my IoT class. It consists of a back end
server with an API to control all the room functionality and a front-end that
can be opened on any web browser to communicate with the raspberry pi server.

## API Routes

The core functionality of the back end exists in the roomServer.py file. This
will run the flask app which specifies the following API routes:

#### '/led-status': GET
This route will return the led status as a json object in the response body.

#### '/alarm-on': GET
A get request to alarm-on will activate the alarm

#### '/alarm-off': GET
A get request to the alarm-off will disarm the alarm

#### '/occupied': GET
This will return wether or not the room is occupied as a json object in the
response body.

#### '/set-led': POST
This route allows the led to be turned on and the color to be set to RED, GREEN,
or BLUE. This route expects a request with a 'color' field specified.

#### '/led-off': GET
This route acts as a convenience function for turning the leds off.


## Running the Server
1. Install required libraries (See Below)
2. Install roomServer.py, ledManager.py, and alarmManager.py all at the same location on the raspberry pi
3. Connect, buzzer to D8 and ultrasonic ranger to D4, also connect LEDS to proper GPIO pins
4. Run roomServer.py with root privileges (for leds)

## Running the dashboard site (Front End)
1. Install the code in Client run on any web server (i.e. Apache)
2. Adjust urls in index.js file to reflect the raspberry pi IP address
3. View the site in a web browser and control the room

## Dependencies (Backend)
GrovePi
Adafruit Nanopixel
Flask

