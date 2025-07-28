"""
Main entry point for the Multi-Level Console Adventure Game.

This is a comprehensive console-based adventure game featuring multiple levels
with increasing difficulty. Players progress through various challenges including
number guessing, word scrambles, math problems, riddles, and a final boss battle.

Features:
- 5 unique levels with different challenge types
- Player progression system with lives, score, and achievements
- Robust error handling and input validation
- Clean, modern console UI with styled text and progress indicators
- Replay functionality and comprehensive statistics

To play: Run this file with Python 3.6+
"""

import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import Game
from utils import print_banner, print_styled_text, clear_screen

def display_welcome_screen():
    """
    Display the initial welcome screen with game information.
    """
    clear_screen()
    
    print_banner("MULTI-LEVEL CONSOLE ADVENTURE", width=70, char="=")
    
    print("🎮 Welcome to the Ultimate Console Adventure Game!")
    print("🌟 A thrilling journey through 5 challenging levels!")
    print()
    print("📋 WHAT AWAITS YOU:")
    print("   🎯 Level 1: Number Detective - Guess the secret number")
    print("   🔤 Level 2: Word Unscrambler - Decode scrambled words")
    print("   🧮 Level 3: Math Wizard - Solve mathematical challenges")
    print("   🧩 Level 4: Riddle Master - Crack mind-bending riddles")
    print("   🐉 Level 5: Ultimate Challenge - Face the final boss!")
    print()
    print("💡 FEATURES:")
    print("   • Progressive difficulty system")
    print("   • Lives and scoring system")
    print("   • Achievement unlocking")
    print("   • Comprehensive statistics")
    print("   • Retry and replay options")
    print()
    print("⚡ REQUIREMENTS:")
    print("   • Python 3.6 or higher")
    print("   • Terminal/Console environment")
    print("   • Keyboard for input")
    print()
    print_styled_text("🚀 Ready to begin your adventure?", "info")
    print()

def check_system_requirements():
    """
    Check if the system meets the minimum requirements.
    
    Returns:
        bool: True if requirements are met, False otherwise
    """
    # Check Python version
    if sys.version_info < (3, 6):
        print_styled_text("❌ Error: Python 3.6 or higher is required!", "error")
        print(f"   Current version: {sys.version}")
        return False
    
    # Check if running in a proper terminal
    if not sys.stdin.isatty():
        print_styled_text("⚠️  Warning: This game is designed for interactive terminal use.", "warning")
        print("   Some features may not work properly in non-interactive environments.")
    
    return True

def main():
    """
    Main function - entry point of the game.
    """
    try:
        # Check system requirements
        if not check_system_requirements():
            print_styled_text("Please upgrade your Python version and try again.", "error")
            sys.exit(1)
        
        # Display welcome screen
        display_welcome_screen()
        
        # Wait for user to start
        input("Press Enter to start your adventure...")
        
        # Create and run the game
        game = Game()
        game.run_game()
        
    except KeyboardInterrupt:
        print_styled_text("\n\n👋 Game interrupted. Thanks for playing!", "info")
        sys.exit(0)
    except Exception as e:
        print_styled_text(f"\n💥 Fatal Error: {e}", "error")
        print_styled_text("Please report this issue if it persists.", "error")
        sys.exit(1)
    finally:
        # Cleanup message
        print_styled_text("\n🎮 Game session ended. Goodbye!", "info")

if __name__ == "__main__":
    main()
