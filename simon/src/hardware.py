import time
from freewili import FreeWili
from freewili.types import FreeWiliProcessorType
from simon.src.constants import (
    SimonColor,
    BASE,
    BUTTON_TO_COLOR,
    COLOR_TO_RGB,
    COLOR_TO_IMG,
    START_SCREEN_NOTEXT,
    START_SCREEN_TEXT,
    GAMEOVER_SCREEN,
    MENU_BUTTON
)

class HardwareHelper():
    def __init__(self):
        self.fw = FreeWili.find_first().expect("No FreeWili found")
        self.fw.open().expect("Failed to open")
        self.fw.reset_display().expect("Failed to reset display")
        self.last = self.fw.read_all_buttons().expect("Failed to read buttons")
        
        self.showStartText()
        self.ledsOff()
        
    def close(self):
        self.ledsOff()
        self.fw.close(restore_menu= True).expect("Failed to close")
        
    # Display Helpers
    
    def showImage(self, path):
        self.fw.show_gui_image(str(path)).expect("failed to show")
        
    def showStartText(self):
        self.showImage(START_SCREEN_TEXT)
        
    def showStartNoText(self):
        self.showImage(START_SCREEN_NOTEXT)

    def showBase(self):
        self.showImage(BASE)
          
    def showColor(self, color: SimonColor):
        self.showImage(COLOR_TO_IMG[color])
        
    def showGameOver(self):
        self.showImage(GAMEOVER_SCREEN)
      
    # LED Helpers
    
    def setAllLEDs(self, r: int, g: int, b: int):
        for i in range(7):
            self.fw.set_board_leds(i, r, g, b).expect("Failed to set LED")
            
    def ledsOff(self):
        self.setAllLEDs(0, 0, 0)
    
    def setLEDColor(self, color: SimonColor):
        r, g, b = COLOR_TO_RGB[color]
        self.setAllLEDs(r, g, b)
        
    # Read Input
    
    def readButton(self):
        start = time.time()
        
        while True:
            buttons = self.fw.read_all_buttons(processor= FreeWiliProcessorType.Main)\
                .expect("Failed to read buttons")
                
            for btnColor, pressed in buttons.items():
                wasPressed = self.last.get(btnColor, False)
                
                if (not wasPressed) and pressed:
                    self.last = buttons
                    
                    if btnColor == MENU_BUTTON:
                        return "MENU"
                    
                    if btnColor == BUTTON_TO_COLOR:
                        return BUTTON_TO_COLOR[btnColor]
                    
                    return None
                
            self.last = buttons