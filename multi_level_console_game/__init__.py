"""
Multi-Level Console Adventure Game

A comprehensive console-based adventure game featuring multiple levels
with increasing difficulty and various challenge types.

Author: BLACKBOXAI
Version: 1.0.0
Python: 3.6+
"""

__version__ = "1.0.0"
__author__ = "BLACKBOXAI"
__description__ = "Multi-Level Console Adventure Game"

# Import main classes for easy access
from .game import Game
from .player import Player
from .level import LEVELS, get_level
from .utils import print_banner, print_styled_text
from .exceptions import LevelError, GameOverError, InvalidInputError

__all__ = [
    'Game',
    'Player', 
    'LEVELS',
    'get_level',
    'print_banner',
    'print_styled_text',
    'LevelError',
    'GameOverError',
    'InvalidInputError'
]
