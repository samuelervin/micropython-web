# Micropython Web
This is a classic starter project for Micropython and an ESP32/ESP8266. It covers the following key concepts in starting with the development on the boards using MicroPython. 
- Connecting to a Wifi Network
- Understanding the GPIO Pins and how to use them (mostly just blinking the onboard IO)
- Active High and Low on Pins and using the Signal class to correct the issue you use plain example code.
- Creating a Socket connection to listen for requests (Socket Communication)
- Injecting information into a simple HTML Web Page simply in order to communicate from the board. 

This does lay the foundation for getting a new board started with development and use it as a boiler plate for development. I also like the fact that with the socket listening you can technically create a bare bones type of API call to the board without returning a web page by changing things over to a JSON return. This is useful if you just want to call an API to trigger reactions, and don't want to rely or wait on things like MQTT to kick things off. Technically you could even use this as a starting point to use one board as a controller then call other boards to do different pieces of work. Up to you, but it is a standard jumping off point. 

# Tutorial Credits and References

- Great starting point if you haven't done this at all before start with flashing <https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/>. Then development setup stuff and intro things <https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/> helps get you setup and running with MicroPython.
- Cause I like VS Code and VS overall I used this one as well. [VS Code Install](https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/)
- <https://randomnerdtutorials.com/micropython-programming-basics-esp32-esp8266/>
- Overall on the listed links there is a lot of good info on the right nav bar. 
- Another good place to go is <https://microcontrollerslab.com/category/micropython-projects-esp32-esp8266/> there are a lot of tutorials and neat projects to check out. 
