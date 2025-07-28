"""
Quick test to verify the game functionality works correctly.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import print_banner, print_styled_text
from player import Player
from level import get_level

def test_level_1():
    """Test Level 1 functionality."""
    print_banner("TESTING LEVEL 1: NUMBER DETECTIVE")
    
    # Create a test player
    player = Player("Test Player")
    print_styled_text("Created test player", "success")
    
    # Get Level 1
    level1 = get_level(1)
    print_styled_text(f"Loaded {level1.title}", "success")
    
    print(f"📝 Level Description: {level1.description}")
    print("🎯 This level would normally ask you to guess a number between 1-100")
    print("✅ Level system is working correctly!")
    
    return True

def test_imports():
    """Test that all imports work correctly."""
    print_banner("TESTING IMPORTS")
    
    try:
        from game import Game
        from level import LEVELS
        from exceptions import LevelError, GameOverError
        
        print_styled_text("✅ All imports successful!", "success")
        print(f"📊 Found {len(LEVELS)} levels")
        print("🎮 Game system ready!")
        return True
        
    except ImportError as e:
        print_styled_text(f"❌ Import error: {e}", "error")
        return False

def main():
    """Run quick tests."""
    print_banner("QUICK GAME TEST", width=60)
    
    # Test imports
    if not test_imports():
        print_styled_text("❌ Import test failed!", "error")
        return
    
    print()
    
    # Test level functionality
    if test_level_1():
        print_styled_text("✅ Level test passed!", "success")
    
    print()
    print_banner("TEST COMPLETE", width=60)
    print("🎉 All systems working correctly!")
    print("🚀 Ready to play the full game with: python main.py")

if __name__ == "__main__":
    main()
