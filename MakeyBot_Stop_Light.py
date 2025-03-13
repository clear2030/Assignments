from gpiozero import LED
import time

red_LED = LED(3) #sets LEDs to pins
yellow_LED = LED(27)
green_LED = LED(10)
traffic_light = {"red_LED":0, "yellow_LED":0, "green_LED":0} #creates dictionary

def stop_light(var): #function that turns the LEDs on and off
    if traffic_light[var] == 0:
        eval(var + ".off()") #uses eval function to turn strings into python commmands
    else:
        eval(var + ".on()")
    
def main():
    print("Welcome to the Makey Bot")
    red_status = int(input("red: ")) #gets user input for LED value (0 or 1)
    yellow_status = int(input("yellow: "))
    green_status = int(input("green: "))
    traffic_light["red_LED"] = red_status #changes the value in the dictionary
    traffic_light["yellow_LED"] = yellow_status
    traffic_light["green_LED"] = yellow_status
    print(traffic_light)
    stop_light("red_LED") #calls the function to turn on/off the LED
    stop_light("yellow_LED")
    stop_light("green_LED")
    
main()
