from enum import Enum, auto
from pathlib import Path
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

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_FWI = PROJECT_ROOT / "simon" / "assets" / "fwi"

START_SCREEN_TEXT = ASSETS_FWI / "start_screen_text.fwi"
START_SCREEN_NOTEXT = ASSETS_FWI / "start_screen_notext.fwi"
GAMEOVER_SCREEN = ASSETS_FWI / "gameover.fwi"
BASE = ASSETS_FWI / "base.fwi"

COLOR_TO_IMG = {
    SimonColor.RED: ASSETS_FWI / "red.fwi",
    SimonColor.BLUE: ASSETS_FWI / "blue.fwi",
    SimonColor.GREEN: ASSETS_FWI / "green.fwi",
    SimonColor.YELLOW: ASSETS_FWI / "yellow.fwi"
}

MENU_BUTTON = ButtonColor.White