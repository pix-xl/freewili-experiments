import random
import time
from enum import Enum, auto
from simon.src.constants import SimonColor
from simon.src.hardware import HardwareHelper

class GameState(Enum):
    START = auto()
    PLAY = auto()
    GAMEOVER = auto()
class SimonGame():
    def __init__(self):
        self.hw = HardwareHelper()
        self.sequence = []
        self.roundNum = 1
        
    def resetGame(self):
        self.sequence = []
        self.roundNum = 1
        
    def randColor(self) -> SimonColor:
        return random.choice(list(SimonColor))
        
    def flash(self, color: SimonColor):
        self.hw.showColor(color)
        self.hw.setLEDColor(color)
        time.sleep(0.75)
        self.hw.showBase()
        self.hw.ledsOff()
        time.sleep(0.75)
        
    def showSequence(self):
        for color in self.sequence:
            self.flash(color)
            
    def playRound(self) -> GameState:
        # Generate a random color at the start of the round
        newColor = self.randColor()
        self.sequence.append(newColor)
        
        # Flash the current sequence
        self.hw.showBase()
        time.sleep(0.5)
        self.showSequence()
        
        # Read player input
        for expected in self.sequence:
            pressed = self.hw.readButton()
            
            # Return to the start screen if menu button is pressed
            if pressed == "MENU":
                return GameState.START
            
            # Show GAMEOVER screena and return to the start screen 
            # if pressed does not equal the expected input
            if pressed != expected:
                return GameState.GAMEOVER
            
        # other wise, the round was successful
        self.roundNum += 1
        return GameState.PLAY
    
    def run(self):
        state = GameState.START
        
        try:
            while True:
                if state == GameState.START:
                    self.resetGame()
                    self.hw.showStartText()
                    self.hw.ledsOff()
                    
                    # Wait for menu button to be pressed and ignore all other input
                    while True:
                        btn = self.hw.readButton()
                        if btn == "MENU":
                            self.hw.showBase()
                            time.sleep(0.25)
                            state = GameState.PLAY
                            break
                    
                elif state == GameState.PLAY:
                    state = self.playRound()
                    if state == GameState.GAMEOVER:
                        self.hw.showGameOver()
                        self.hw.ledsOff()
                        
                elif state == GameState.GAMEOVER:
                    # Wait for the menu button to be pressed to restart
                    while True:
                        btn = self.hw.readButton()
                        if btn == "MENU":
                            state = GameState.START
                            break
        except KeyboardInterrupt:
            pass
        
        finally:
            self.hw.close()