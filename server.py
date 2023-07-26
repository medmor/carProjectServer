from bottle import post, route, run

@route("/")
def index():
    return "Rc Car Server"


@route("/right")
def right():
    return "Car turning right"


@route("/left")
def left():
    return "Car turning left"


@route("/center")
def center():
    return "Car turning center"


@route("/forward/<speed>")
def forward(speed):
    return "Car running froward at speed : " + speed


@route("/backward/<speed>")
def backward(speed):
        return "Car running backward at speed : " + speed


@route("/stop")
def stop():
        return "Car stopped, the speed is : 0"

run(host="0.0.0.0", port=8080)