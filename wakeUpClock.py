# Wake-Up Clock

import time
import datetime
import pygame

def setAlarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    soundFile = "Dream Big - Jeremy Korpas.mp3"
    isRunning = True

    while isRunning:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S") 
        print(currentTime)

        if currentTime == alarm_time:  
            print("WAKE UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(soundFile)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            isRunning = False

if __name__ == "__main__":
    user_alarm_time = input("Enter the alarm time (HH:MM:SS): ")  
    setAlarm(user_alarm_time) 