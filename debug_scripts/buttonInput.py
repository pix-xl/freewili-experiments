import time
from freewili import FreeWili
from freewili.types import FreeWiliProcessorType

def main():
    with FreeWili.find_first().expect("Failed to find a FreeWili") as device:
        device.open().expect("Failed to open")
    
        print("Reading Buttons... Ctrl + C to exit")
        last = device.read_all_buttons(processor= FreeWiliProcessorType.Display)\
            .expect("Failed to read buttons")
        
        try:
            while True:
                buttons = device.read_all_buttons(processor= FreeWiliProcessorType.Display)\
                    .expect("Failed to read buttons")

                for color, state in buttons.items():
                    if last[color] != state:
                        print(f"{color.name}:   {'True' if state else 'False'}")
                
                last = buttons
                
        #ignore all keyboard input
        except KeyboardInterrupt:
            pass
        
        finally:
            device.close()


if __name__ == "__main__":
    main()