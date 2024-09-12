import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials, db




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
            
cred = credentials.Certificate('/home/x120612032/2222/gaiabitplzzz-firebase-adminsdk-u013f-9353823e8b.json')
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://gaiabitplzzz-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
                        

def listen_for_count_change():
    ref = db.reference('/Count')
    ref.listen(handle_count_change)
    
            
def handle_count_change(event):
    new_count = event.data
    if new_count in [0, 90, 180, 360]:
        rotate_motor(new_count)
        
    
if __name__ == "__main__":
    setup_motor()
    listen_for_count_change()
   
            
