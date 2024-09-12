import RPi.GPIO as GPIO
import time

IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

def setup_motor():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(IN1, GPIO.OUT)
	GPIO.setup(IN2, GPIO.OUT)
	GPIO.setup(IN3, GPIO.OUT)
	GPIO.setup(IN4, GPIO.OUT)
	
sequence = [
    [1,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

def rotate_motor(degrees):
    steps_per_revolution = 512
    step_count = int(steps_per_revolution * degrees / 360)
    for _ in range(step_count):
        for step in sequence:
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(0.001)

if __name__ == "__main__":
	try:
		setup_motor()
		rotate_motor(90)
		GPIO.cleanup()
	except Exception as e:
		print(f"ERROR-E -{e}")
		GPIO.cleanup()
