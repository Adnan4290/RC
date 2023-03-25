import os
import time

def switch_camera():
    # Define the GPIO pins for the camera multiplexer
    gpio_17 = 17
    gpio_4 = 4
    
    # Check which camera is currently selected
    camera_a_selected = False
    camera_b_selected = False
    if os.system("raspi-gpio get {}".format(gpio_17)) == 0:
        camera_a_selected = True
    elif os.system("raspi-gpio get {}".format(gpio_4)) == 0:
        camera_b_selected = True
    
    # Switch to the other camera
    if camera_a_selected:
        print("Switching to Camera B")
        os.system("raspi-gpio set {} op".format(gpio_17))
        os.system("raspi-gpio set {} dl".format(gpio_17))
        os.system("raspi-gpio set {} dh".format(gpio_4))
        time.sleep(1)  # Allow time for the camera to release all locks
        os.system("i2cset -y 1 0x70 0x00 0x02")
        print("camea b selected")
    elif camera_b_selected:
        print("Switching to Camera A")
        os.system("raspi-gpio set {} op".format(gpio_4))
        os.system("raspi-gpio set {} dl".format(gpio_4))
        os.system("raspi-gpio set {} dh".format(gpio_17))
        time.sleep(1)  # Allow time for the camera to release all locks
        os.system("i2cset -y 1 0x70 0x00 0x01")
        print("camera a selected")
    else:
        print("No camera selected")
