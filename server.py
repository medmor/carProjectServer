from bottle import post, route, static_file, run
from car import Motor, Car

car = Car(Motor(23, 24), Motor(18, 15, 14))

@route("/")
def index():
    return static_file("index.html", root="./")

@post("/right")
def right():
    car.turnRight()

@post("/left")
def left():
    car.turnLeft()

@post("/center")
def center():
    car.resetDir()

@post("/forward")
def forward():
    car.runForward()

@post("/forward/<amount>")
def forwardWithSpeed(amount):
    car.setSpeed(int(amount))
    car.runForward()

@post("/backward")
def backward():
    car.runBackward()

@post("/backward/<amount>")
def backwardWithSpeed(amount):
    car.setSpeed(int(amount))
    car.runBackward()

@post("/speed/<amount>")
def speed(amount):
    car.setSpeed(int(amount))

@post("/stop")
def stop():
    car.stop()

@post("/siren")
def siren():
    car.siren()


run(host="0.0.0.0", port=8080, debug=True)

