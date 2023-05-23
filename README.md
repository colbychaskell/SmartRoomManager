# Smart Room Manager 

To run the program:
1. Install required libraries (See Below)
2. Install roomServer.py, ledManager.py, and alarmManager.py all at the same location on the raspberry pi
3. Connect, buzzer to D8 and ultrasonic ranger to D4, also connect LEDS to proper GPIO pins
4. Run roomServer.py with root privileges (for leds) 
5. Install the front end and run on any server (adjust urls in js file to reflect rpi IP address)
6. Connect to front end from any device and control room


REQUIRED LIBRARIES:
GrovePi
Adafruit Nanopixel
Flask

