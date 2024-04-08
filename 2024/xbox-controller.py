import xbox
import pigpio
from lib.docyke_servo import docyke_servo

print("START");


def show(*args):
    for arg in args:
        print(arg, end="")


def steer(joystick_pos):
    servo.set_angle(180 + 180 * joystick_pos)


pi = pigpio.pi()
joy = xbox.Joystick()
servo = docyke_servo(pi)

try:
    while not joy.Back():
        steer(joy.leftX())


finally:
    # Close out when done
    joy.close()
