import time
from freewili import FreeWili
from .constants import (
    SimonColor,
    BUTTON_TO_COLOR,
    COLOR_TO_BUTTON,
    COLOR_TO_RGB,
    MENU_BUTTON
)

class hardwareHelper():
    def __init__(self):
        self.fw = FreeWili.find_first().expect("No FreeWili found")
        self.fw.open().expect("Failed to open")
        self.fw.resetDisplay().expect("Failed to reset display")
        self.last = self.fw.read_all_buttons().expect("Failed to read buttons")
        
        self.showBase()
        self.ledsOff()
        
    def close(self):
        self.ledsOff()
        self.fw.close(restore_menu= True)