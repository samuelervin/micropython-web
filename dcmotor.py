class DCMotor:      
#initialize the class with values
#     pin1 corresponds to the GPIO pin connected with IN1 (input 1). This is GPIO5 in our case.
#     pin2 corresponds to the GPIO pin connected with IN2 (input 2). This is GPIO4 in our case. Both these pins are configured as outputs.
#     enable_pin is the GPIO PWM pin connected with ENA (Enable of motor A).
#     min_duty is the minimum duty cycle which is required for the motor to start. This can be changed according to the frequency required for the motor to spin and is set to 750 as default.
#     max_duty is the maximum duty cycle required to start the motor. It is set to 1023 as default. This can also be changed according to the frequency.
  def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1=pin1
        self.pin2=pin2
        self.enable_pin=enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty
#sends signal to the pin to move the motor in a forward motion. For a single direction motor use only this. 
  def forward(self,speed):
    self.speed = speed
    self.enable_pin.duty(self.duty_cycle(self.speed))
    self.pin1.value(0)
    self.pin2.value(1)
 #sends a signal to the pin to move the motor in a reverse motion.    
  def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)
        
#sends a full stop to the motor for both pins
  def stop(self):
    self.enable_pin.duty(0)
    self.pin1.value(0)
    self.pin2.value(0)
#duty cycle     
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle