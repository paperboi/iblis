from plyer import notification
from time import sleep
import psutil
def sendNotification(title, message):
    notification.notify(
        title,
        message=message,
        app_icon='logo.ico',
        timeout=3,
        ticker='iblis',
        toast='True'
    )
batteryPercent = psutil.sensors_battery().percent
batteryPowerPlugged = psutil.sensors_battery().power_plugged

while(True):
    # To notify the user whenever the laptop charger is plugged in or not
    if psutil.sensors_battery().power_plugged != batteryPowerPlugged:
        if batteryPowerPlugged == True:
            sendNotification('Plugged in, charging', f'{batteryPercent}% remaining')
        sendNotification('On battery power', f'{batteryPercent}% remaining')

    # To record any change in either battery% or whether the device is plugged in or not
    if psutil.sensors_battery().percent != batteryPercent:
        batteryPercent = psutil.sensors_battery().percent
        batteryPowerPlugged = psutil.sensors_battery().power_plugged

        # checkForConditions()
        if batteryPercent == 40 and batteryPowerPlugged == False:
            sendNotification(f'You might want to plug in your PC.', '40% remaining')
        if batteryPercent == 80 and batteryPowerPlugged == True:
            sendNotification(f'You might want to unplug your PC from the power supply.', '80% remaining')