try:
    import sdl2.ext
except ImportError:
    print "Missing pySDL2 for gui"

from btcoms import *

# Set up btSerial here:

#

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Driver Software", size=(800, 600))
    window.show()
    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

            if event.type == sdl2.
            
        window.refresh()
    return 0


if __name__ == "__main__":
    run()

