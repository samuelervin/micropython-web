def writeDoorState():
     settings_dict['DoorState'] = door_state
     settings_dict['LEDState'] = led_state
     print(settings_dict['DoorState'])
     with open('settings.json', 'w') as json_file:
        json.dump(settings_dict, json_file)
  
def openDoor():
    dc_motor.forward(50)
    time.sleep(25)
    dc_motor.stop()
    print("The door is AJAR!")

def closeDoor():
    dc_motor.backwards(50)
    time.sleep(25)
    dc_motor.stop()
    print("The door is CLOSED!")

def web_page():
    html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #0066ff;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #ff6319;
        }
    </style>
</head>

<body>
    <h2>ESP MicroPython Web Server</h2>
    <p>LED state: <strong>""" + led_state + """</strong></p>
    <i class="fas fa-lightbulb fa-3x" style="color:#""" + color + """;"></i>
    <p>Door state: <strong>""" + door_state + """</strong></p>
    <p>
        <a href=\"?led_2_on\"><button class="button">LED ON</button></a>
    </p>
    <p>
        <a href=\"?led_2_off\"><button class="button button1">LED OFF</button></a>
    </p>
</body>

</html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        
        led_on = request.find('/?led_2_on')
        led_off = request.find('/?led_2_off')
        
        if led_on == 6:
            print('LED ON -> GPIO2')
            led_state = "ON"
            door_state = "OPEN"
            color = "d8dc55"
            led.on()
        if led_off == 6:
            print('LED OFF -> GPIO2')
            led_state = "OFF"
            door_state = "CLOSED"
            led.off()
            color = "000000"
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
        print(door_state)
        if door_state == "OPEN":
            openDoor()
        if door_state == "CLOSED":
            closeDoor()
        writeDoorState()
    except OSError as e:
        conn.close()
        print('Connection closed')
        machine.reset()
