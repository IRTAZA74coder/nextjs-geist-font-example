"""
Custom exceptions for the multi-level console game.
"""

class InvalidInputError(Exception):
    """
    Raised when user provides invalid input that cannot be processed.
    """
    pass

class LevelError(Exception):
    """
    Raised when an error occurs during level execution.
    """
    pass

class GameOverError(Exception):
    """
    Raised when the game should end due to player failure.
    """
    pass
