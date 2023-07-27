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


@post("/forward/<amount>")
def forward(amount):
    car.setSpeed(int(amount))
    car.runForward()


@post("/backward/<amount>")
def backward(amount):
    car.setSpeed(int(amount))
    car.runBackward()


@post("/stop")
def stop():
    car.setSpeed(0)
    car.stop()

@post("/siren")
def siren():
    print("siren")
    car.siren()


run(host="0.0.0.0", port=8080, debug=True)

