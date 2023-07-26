import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class Motor:
    def __init__(self, io1: int, io2: int, io3=-1) -> None:
        self.io1 = io1
        self.io2 = io2
        GPIO.setup(io1, GPIO.OUT)
        GPIO.setup(io2, GPIO.OUT)
        if io3 > 0:
            GPIO.setup(io3, GPIO.OUT)
            self.io3 = GPIO.PWM(io3, 1000)
            self.io3.start(50)

    def forward(self):
        GPIO.output(self.io1, GPIO.HIGH)
        GPIO.output(self.io2, GPIO.LOW)

    def backward(self):
        GPIO.output(self.io1, GPIO.LOW)
        GPIO.output(self.io2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.io1, GPIO.LOW)
        GPIO.output(self.io2, GPIO.LOW)

    def setSpedd(self, speed: int):
        self.io3.ChangeDutyCycle(speed)


class Car:
    def __init__(self, frontMotor: Motor, backMotor: Motor) -> None:
        self.frontMotor = frontMotor
        self.backMotor = backMotor

    def turnRight(self):
        self.frontMotor.forward()

    def turnLeft(self):
        self.frontMotor.backward()

    def resetDir(self):
        self.frontMotor.stop()

    def runForward(self):
        self.backMotor.forward()

    def runBackward(self):
        self.backMotor.backward()

    def stop(self):
        self.backMotor.stop()

    def setSpeed(self, speed: int):
        self.backMotor.setSpedd(speed)

    def cleanup():
        GPIO.cleanup()
