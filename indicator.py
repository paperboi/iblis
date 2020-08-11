from plyer import notification
from time import sleep
import psutil

def sendNotification(message):
    notification.notify(
        title=f'{psutil.sensors_battery().percent}% remaining',
        message=message,
        app_icon='logo.ico',
        timeout=10,
    )
batteryPercent = psutil.sensors_battery().percent
batteryPowerPlugged = psutil.sensors_battery().power_plugged

def checkForConditions():
    if batteryPercent == 40 and batteryPowerPlugged == False:
        sendNotification(f'You might want to plug in your PC.')
    if batteryPercent == 80 and batteryPowerPlugged == True:
        sendNotification(f'You might want to unplug your PC from the power supply.')

while(True):
    if psutil.sensors_battery().percent != batteryPercent or psutil.sensors_battery().power_plugged != batteryPowerPlugged:
        batteryPercent = psutil.sensors_battery().percent
        batteryPowerPlugged = psutil.sensors_battery().power_plugged
        checkForConditions()