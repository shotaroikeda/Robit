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


def move_signal(btserial, comm, wait_for=False, sleep_time=0.1):
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

    # Wait for movement to finish
    if wait_for:
        comm_num = int(comm)
        comm_num /= 100
        time.sleep(comm_num)

    ret = btserial.readline()

    try:
        return int(ret.strip())
    except ValueError:
        print "Bad value was returned (could be a problem)"
        return ret.strip()

