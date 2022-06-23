import pypsutil
from pynotifier import Notification
import winsound
battery=pypsutil.sensors_battery_total()
plugged=battery.power_plugged
percent=battery.percent

if percent>=20:
    freq=500
    dur=100

    winsound.Beep(freq,dur)
    Notification(
        title="Battery low",
        description=str(percent)+"% battery remain !!",
        duration=10     ,
        # urgency=Notification.URGENCY_CRITICAL,
    ).send()