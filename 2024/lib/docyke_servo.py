class docyke_servo:
    pi = None
    gpio = None
    min_pwm = None
    max_pwm = None
    zero_pwm = None
    motor_range_pwm = None
    max_angle = None
    min_angle = None

    def __init__(self, pi, gpio=12, min_pwm=500, max_pwm=2500, max_angle=360, min_angle=0):
        """
        Creates a docyke_servo object
        :param pi: The pigpio object
        :param gpio: The GPIO pin the servo's signal pin is connected to (default 12)
        :param min_pwm: The minimum PWM the servo can handle, in microseconds (default 500)
        :param max_pwm: THe maximum PWM the servo can handle, in microseconds (default 2500)
        """
        self.pi = pi
        self.gpio = gpio
        self.min_pwm = min_pwm
        self.max_pwm = max_pwm
        self.zero_pwm = (max_pwm + min_pwm) / 2
        self.motor_range_pwm = max_pwm - self.zero_pwm
        self.range_pwm = max_pwm - min_pwm
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.range_angle = max_angle - min_angle

    def set_speed(self, speed, clockwise: bool):
        """
        Sets the speed of the servo
        :param speed: The speed of the servo. 1.0 is full speed, 0.0 is full stop.
        :param clockwise: Whether the servo should move clockwise or not. Expects a bool. True means move clockwise
        """
        speed = min(max(0.0, speed), 1.0)  # ensures the speed is a percentage value
        self.pi.set_servo_pulsewidth(self.gpio, self.zero_pwm + ((speed if clockwise else -speed) * self.motor_range_pwm))

    def stop(self):
        """
        Stops the servo
        :return:
        """
        self.pi.set_servo_pulsewidth(self.gpio, self.zero_pwm)

    def set_angle(self, angle):
        p = float(max(min(angle, self.max_angle), self.min_angle) - self.min_angle) / self.range_angle
        pwm = int(p * self.range_pwm + self.min_pwm)
        self.pi.set_servo_pulsewidth(self.gpio, pwm)

    def set_angle_zero(self):
        self.set_angle(0)
        
