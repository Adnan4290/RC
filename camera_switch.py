import RPi.GPIO as GPIO
import time

def switch_camera():
    # Define the GPIO pins for the camera multiplexer
    gpio_17 = 17
    gpio_4 = 4
    
    # Set GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set GPIO pin modes
    GPIO.setup(gpio_17, GPIO.OUT)
    GPIO.setup(gpio_4, GPIO.OUT)
    
    # Check which camera is currently selected
    camera_a_selected = False
    camera_b_selected = False
    if GPIO.input(gpio_17) == 1:
        camera_a_selected = True
    elif GPIO.input(gpio_4) == 1:
        camera_b_selected = True
    
    # Switch to the other camera
    if camera_a_selected:
        print("Switching to Camera B")
        GPIO.output(gpio_17, GPIO.LOW)
        GPIO.output(gpio_4, GPIO.HIGH)
        time.sleep(1)  # Allow time for the camera to release all locks
        os.system("i2cset -y 1 0x70 0x00 0x02")
        print("Camera B selected")
    elif camera_b_selected:
        print("Switching to Camera A")
        GPIO.output(gpio_4, GPIO.LOW)
        GPIO.output(gpio_17, GPIO.HIGH)
        time.sleep(1)  # Allow time for the camera to release all locks
        os.system("i2cset -y 1 0x70 0x00 0x01")
        print("Camera A selected")
    else:
        print("No camera selected")
