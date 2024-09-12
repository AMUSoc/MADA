import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

servo1 = GPIO.PWM(23, 50)
servo1.start(0)

def angle_to_duty_cycle(angle):
    return (angle / 18) + 2.5

try:
    while True:
        for angle in [0, 45, 90, 135, 180]:
            dc = angle_to_duty_cycle(angle)
            servo1.ChangeDutyCycle(dc)
            print(f"Setting servo to angle {angle}")
            time.sleep(1)

        for angle in [180, 135, 90, 45, 0 ]:
            dc = angle_to_duty_cycle(angle)
            servo1.ChangeDutyCycle(dc)
            print(f"Setting servo to angle {angle}")
            time.sleep(1)

finally:
    servo1.stop()
    GPIO.cleanup()

