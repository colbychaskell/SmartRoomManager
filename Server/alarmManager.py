from grovepi import *
from grove_rgb_lcd import *

# GROVEPI configuration
USR_PORT = 4
BUZZER_PORT = 8

pinMode(BUZZER_PORT, "OUTPUT")

class alarmManager(object):
    def __init__(self):
        self.occupied = "Unoccupied"
        self.alarm_status = "Off"

    def set_alarm_on(self):
        self.alarm_status = "On"

    def set_alarm_off(self):
        self.alarm_status = "Off"
        digitalWrite(BUZZER_PORT, 0)

    def detect_motion(self):
        detection_count = 0 # To avoid false pos, need 5 readings in a row of an object in range
        while self.alarm_status == "On":
            try:
                usr = ultrasonicRead(USR_PORT)

                if self.occupied == "Unoccupied": 
                    if(usr < 250):
                        detection_count += 1
                    else:
                        detection_count = 0

                    if(detection_count >= 6):
                        detection_count = 0
                        print("Occupied")
                        digitalWrite(BUZZER_PORT,1) # Trigger Buzzer/Alarm
                        self.occupied = "Occupied"	
                else:
                    if(usr > 250):
                        detection_count += 1
                    else:
                        detection_count = 0

                    if(detection_count >= 15): # Less sensitive on turning off, more sensitive on turning on for user responsiveness
                        detection_count = 0
                        print("Unoccupied")
                        digitalWrite(BUZZER_PORT,0)
                        self.occupied = "Unoccupied"	

                time.sleep(0.2)
            except KeyboardInterrupt:
                digitalWrite(BUZZER_PORT, 0)
                break
        print("Motion Detection Off")

