#Libraries
import RPi.GPIO as GPIO
import time
import random
from gpiozero import Motor
 
leftCounter = 0
rightCounter = 0

#Timeout
maxtime_right = 0.04
maxtime_middle = 0.04
maxtime_left = 0.04

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGERright =24
GPIO_ECHOright = 23

GPIO_TRIGGERmiddle = 15
GPIO_ECHOmiddle = 14

GPIO_TRIGGERleft = 8
GPIO_ECHOleft = 25

#Setting Motors
motorleft = Motor(26, 19)
motorright = Motor(13, 6)

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGERmiddle, GPIO.OUT)
GPIO.setup(GPIO_ECHOmiddle, GPIO.IN)

GPIO.setup(GPIO_TRIGGERright, GPIO.OUT)
GPIO.setup(GPIO_ECHOright, GPIO.IN)

GPIO.setup(GPIO_TRIGGERleft, GPIO.OUT)
GPIO.setup(GPIO_ECHOleft, GPIO.IN)

def distanceMid():

    GPIO.output(GPIO_TRIGGERmiddle, False)
    time.sleep(0.01)

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGERmiddle, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGERmiddle, False)

    StartTime = time.time()
    timeout_mid = StartTime + maxtime_middle

    # save StartTime
    while GPIO.input(GPIO_ECHOmiddle) == 0 and StartTime < timeout_mid:
        StartTime = time.time()

    StopTime = time.time()
    timeout_mid = StopTime + maxtime_middle

        # save time of arrival
    while GPIO.input(GPIO_ECHOmiddle) == 1 and StopTime < timeout_mid:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = TimeElapsed * 17150
    distance = round(distance, 2)

    return distance

def distanceLeft():

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGERleft, False)
    time.sleep(0.01)

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGERleft, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGERleft, False)

    StartTime = time.time()
    timeout_left = StartTime + maxtime_left

    # save StartTime
    while GPIO.input(GPIO_ECHOleft) == 0 and StartTime < timeout_left:
        StartTime = time.time()

    StopTime = time.time()
    timeout_left = StopTime + maxtime_left

    # save time of arrival
    while GPIO.input(GPIO_ECHOleft) == 1 and StopTime < timeout_left:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = TimeElapsed * 17150
    distance = round(distance, 2)

    return distance

def distanceRight():

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGERright, False)
    time.sleep(0.01)

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGERright, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGERright, False)

    StartTime = time.time()
    timeout_right = StartTime + maxtime_right

    # save StartTime
    while GPIO.input(GPIO_ECHOright) == 0 and StartTime < timeout_right:
        StartTime = time.time()

    StopTime = time.time()
    timeout_right = StopTime + maxtime_right

    # save time of arrival
    while GPIO.input(GPIO_ECHOright) == 1 and StopTime < timeout_right:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = TimeElapsed * 17150
    distance = round(distance, 2)

    return distance


if __name__ == '__main__':
    try:
        while True:

            #motorleft.forward(0.35)
            #motorright.forward(0.35)

            distMid = distanceMid()
            print ("Middle Distance = %.1f cm" % distMid)
            time.sleep(0.05)

            distRight = distanceRight()
            print ("Right Distance = %.1f cm" % distRight)
            time.sleep(0.05)

            distLeft = distanceLeft()
            print ("Left Distance = %.1f cm" % distLeft)
            time.sleep(0.05)

            if distLeft < 15.0:
                rightCounter += 1
                motorleft.stop()
                motorright.stop()
                time.sleep(1)

                motorleft.forward(0.35)
                motorright.backward(0.35)
                time.sleep(0.4)

                motorleft.stop()
                motorright.stop()
                time.sleep(1)

            elif distRight < 15.0:
                leftCounter += 1
                motorleft.stop()
                motorright.stop()
                time.sleep(1)

                motorleft.backward(0.35)
                motorright.forward(0.35)
                time.sleep(0.4)

                motorleft.stop()
                motorright.stop()
                time.sleep(1)

            elif distMid < 25.0:

                motorleft.stop()
                motorright.stop()
                time.sleep(1)

                motorleft.backward(0.35)
                motorright.backward(0.35)
                time.sleep(1)

                #THIS SHIT GO LEFT
                if leftCounter = rightCounter:
                    X = random.randint(0,1)
                    
                    #this shit go left
                    if X == 0:
                        leftCounter += 1
                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)

                        motorleft.backward(0.35)
                        motorright.forward(0.35)
                        time.sleep(0.4)

                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)

                    #THIS SHIT GO RIGHT
                    else:
                        rightCounter += 1
                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)

                        motorleft.forward(0.35)
                        motorright.backward(0.35)
                        time.sleep(0.4)

                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)
                        
                    elif leftCounter > rightCounter:
                        rightCounter += 1
                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)

                        motorleft.forward(0.35)
                        motorright.backward(0.35)
                        time.sleep(0.4)

                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)
                        
                    elif rightCounter > leftCounter:
                        leftCounter += 1
                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)

                        motorleft.backward(0.35)
                        motorright.forward(0.35)
                        time.sleep(0.4)

                        motorleft.stop()
                        motorright.stop()
                        time.sleep(1)
                        
    
    except KeyboardInterrupt:
        GPIO.cleanup()

    finally:
        # Stop the motors, even if there is an exception
        # or the user presses Ctrl+C to kill the process.
        motorright.stop()
        motorleft.stop()
        GPIO.cleanup()
