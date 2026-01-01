from enum import Enum, auto
from freewili import FreeWili
from freewili.types import ButtonColor

class SimonColor(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    
COLOR_TO_BUTTON = {
    SimonColor.RED: ButtonColor.Red,
    SimonColor.BLUE: ButtonColor.Blue,
    SimonColor.GREEN: ButtonColor.Green,
    SimonColor.YELLOW: ButtonColor.Yellow
}

BUTTON_TO_COLOR = {
    v:
        k for k, v in COLOR_TO_BUTTON.items()
}

COLOR_TO_RGB = {
    SimonColor.RED: (255, 0, 0),
    SimonColor.BLUE: (0, 0, 255),
    SimonColor.GREEN: (0, 255, 0),
    SimonColor.YELLOW: (255, 180, 0)
}

COLOR_TO_IMG = {
    "Base" : "/simon/assets/fwi/base.fwi",
    SimonColor.RED: "/simon/assets/fwi/red.fwi",
    SimonColor.BLUE: "/simon/assets/fwi/blue.fwi",
    SimonColor.GREEN: "/simon/assets/fwi/green.fwi",
    SimonColor.YELLOW: "/simon/assets/fwi/yellow.fwi"
}

START_SCREEN_TEXT = "/simon/assets/fwi/start_screen_text.fwi"
START_SCREEN_NOTEXT = "/simon/assets/fwi/start_screen_notext.fwi"
GAMEOVER_SCREEN = "/simon/assets/fwi/gameover.fwi"

MENU_BUTTON = ButtonColor.White