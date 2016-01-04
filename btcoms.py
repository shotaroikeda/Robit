try:
    import sdl2.ext
    import serial
except ImportError:
    print "Please Install required packages"

import time

def init_serial(device="/dev/cu.HC-05-DevB", baud=9600):
    """
    Initializes the bluetooth device for serial communication
    TODO: Make sure the serial gets closed later.
    """
    btserial = serial.Serial(device, baud)
    return btserial


def move_signal(btserial, comm, sleep_time=0.1):
    """
    Send a signal to the hardware.

    Please see the documentation for details.
    """

    if type(comm) == int:
        comm = str(comm)

    btserial.write(comm)

    # Wait time can be variable based off of connectivity
    # Change the value if it's too small
    time.sleep(sleep_time)  # 0.1 Default
    ret = btserial.readline()

    return ret


def _test():
    print "Initializing btSerial"
    btserial = init_serial()
    
    print "Testing sending signal..."

if __name__ == '__main__':
    print "Testing the motors"
    
