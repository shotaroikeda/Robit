try:
    import sdl2.ext
except ImportError:
    print "Missing pySDL2 for gui"

from btcoms import *


def run(t=True, btSerial=None):
    if t:
        run_no_serial()
    elif btSerial is None:
        print "No btSerial was passed, running test segment"
        run_no_serial()
    else:
        run_with_serial(btSerial)

        
def run_with_serial(btSerial):
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

            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    # Move the Robit Up
                    print "Move up detected"
                    move_signal(btSerial, 190, True)
                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    print "Move down detected"
                    move_signal(btSerial, 193, True)
                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    print "Move left detected"
                    move_signal(btSerial, 192, True)
                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    print "Move right detected"
                    move_signal(btSerial, 191, True)
                elif event.key.keysym.sym == sdl2.SDLK_SPACE:
                    print "Force all to stop"
                    move_signal(btSerial, 115)
                    break

            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDLK_LEFT, sdl2.SDLK_DOWN, sdl2.SDLK_RIGHT):
                    print "Key lifted"

        window.refresh()

        # Make sure the cpu doesn't blow up by forcing thread to sleep
        time.sleep(0.016)  # Buttery 60 fps

    return 0


def run_no_serial():
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

            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_DOWN:
                    # Move the Robit Down
                    print "Move down detected"
                elif event.key.keysym.sym == sdl2.SDLK_UP:
                    print "Move up detected"
                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    print "Move right detected"
                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    print "Move left detected"

            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDLK_LEFT, sdl2.SDLK_DOWN, sdl2.SDLK_RIGHT):
                    print "Key lifted"

        window.refresh()
    return 0


if __name__ == "__main__":
    # Set up btSerial here:
    btSerial = init_serial() 
    run(False, btSerial)
