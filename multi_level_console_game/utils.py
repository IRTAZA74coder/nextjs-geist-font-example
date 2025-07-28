"""
Utility functions for user interface and input handling.
"""

import os
import sys
from typing import List, Optional, Union

def print_banner(text: str, width: int = 60, char: str = "=") -> None:
    """
    Print a styled banner with the given text.
    
    Args:
        text: The text to display in the banner
        width: Width of the banner
        char: Character to use for the border
    """
    print("\n" + char * width)
    print(f"{text:^{width}}")
    print(char * width + "\n")

def print_separator(width: int = 60, char: str = "-") -> None:
    """
    Print a separator line.
    
    Args:
        width: Width of the separator
        char: Character to use for the separator
    """
    print(char * width)

def get_input(prompt: str, valid_options: Optional[List[str]] = None, 
              input_type: str = "string") -> Union[str, int]:
    """
    Get validated input from the user.
    
    Args:
        prompt: The prompt to display to the user
        valid_options: List of valid string options (case-insensitive)
        input_type: Type of input expected ("string", "int", "yes_no")
    
    Returns:
        The validated user input
    
    Raises:
        KeyboardInterrupt: If user presses Ctrl+C
    """
    while True:
        try:
            user_input = input(f"{prompt}: ").strip()
            
            if input_type == "int":
                try:
                    return int(user_input)
                except ValueError:
                    print("❌ Please enter a valid number.")
                    continue
            
            elif input_type == "yes_no":
                if user_input.lower() in ['y', 'yes', '1']:
                    return 'yes'
                elif user_input.lower() in ['n', 'no', '0']:
                    return 'no'
                else:
                    print("❌ Please enter 'y' for yes or 'n' for no.")
                    continue
            
            elif valid_options:
                if user_input.lower() in [option.lower() for option in valid_options]:
                    return user_input.lower()
                else:
                    print(f"❌ Please choose from: {', '.join(valid_options)}")
                    continue
            
            else:
                if user_input:
                    return user_input
                else:
                    print("❌ Please enter a valid response.")
                    continue
                    
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for playing! Goodbye!")
            sys.exit(0)

def clear_screen() -> None:
    """
    Clear the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_styled_text(text: str, style: str = "normal") -> None:
    """
    Print text with basic styling using Unicode characters.
    
    Args:
        text: The text to print
        style: Style type ("success", "error", "warning", "info", "normal")
    """
    styles = {
        "success": "✅ ",
        "error": "❌ ",
        "warning": "⚠️  ",
        "info": "ℹ️  ",
        "normal": ""
    }
    
    prefix = styles.get(style, "")
    print(f"{prefix}{text}")

def display_progress_bar(current: int, total: int, width: int = 30) -> None:
    """
    Display a simple progress bar.
    
    Args:
        current: Current progress value
        total: Total/maximum value
        width: Width of the progress bar
    """
    if total == 0:
        percentage = 0
    else:
        percentage = min(100, (current / total) * 100)
    
    filled = int(width * current // total) if total > 0 else 0
    bar = "█" * filled + "░" * (width - filled)
    
    print(f"Progress: [{bar}] {percentage:.1f}% ({current}/{total})")
