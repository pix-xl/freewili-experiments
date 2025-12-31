import time
from freewili import FreeWili
from freewili.types import FreeWiliProcessorType

def main():
    with FreeWili.find_first().expect("Failed to find a FreeWili") as device:
        device.open().expect("Failed to open")
        
        try: 
            while True:
                for i in range(7):
                    device.set_board_leds(i, 20, 0 ,0).expect("Failed to set LEDs")
                    time.sleep(0.5)
                    device.set_board_leds(i, 0, 0 ,0).expect("Failed to set LEDs")
        
        except KeyboardInterrupt:
            pass
        
        finally:
            #turn all LEDs off
            for i in range(7):
                device.set_board_leds(i, 0, 0, 0).expect("Failed to set LEDs")
            device.close()
    
if __name__ == "__main__":
    main()