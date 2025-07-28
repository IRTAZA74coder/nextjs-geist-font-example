"""
Demo script to showcase the Multi-Level Console Adventure Game functionality.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from player import Player
from level import get_level, LEVELS
from utils import print_banner, print_styled_text, print_separator
from game import Game

def demo_player_system():
    """Demonstrate the player system."""
    print_banner("PLAYER SYSTEM DEMO")
    
    # Create a player
    player = Player("Demo Hero")
    print_styled_text("Created new player!", "success")
    player.display_status()
    
    # Simulate some gameplay
    print("\n🎮 Simulating gameplay...")
    player.update_score(50)
    player.add_achievement("Demo Achievement")
    player.add_to_inventory("Magic Sword")
    player.take_damage(20)
    
    print_styled_text("After some gameplay:", "info")
    player.display_status()
    
    print_separator()

def demo_level_system():
    """Demonstrate the level system."""
    print_banner("LEVEL SYSTEM DEMO")
    
    print(f"📊 Total levels available: {len(LEVELS)}")
    print("\n🎯 Level Overview:")
    
    for i, level in enumerate(LEVELS, 1):
        print(f"   Level {i}: {level.title}")
        print(f"   Description: {level.description}")
        print()
    
    print_separator()

def demo_game_features():
    """Demonstrate key game features."""
    print_banner("GAME FEATURES DEMO")
    
    print("✨ Key Features:")
    print("   • 5 Progressive Levels with increasing difficulty")
    print("   • Lives system (3 lives per game)")
    print("   • Comprehensive scoring system")
    print("   • Achievement unlocking")
    print("   • Retry functionality for failed levels")
    print("   • Modern console UI with styled text")
    print("   • Robust error handling and input validation")
    print("   • Comprehensive game statistics")
    print("   • Replay functionality")
    print()
    
    print("🎮 Level Types:")
    print("   🎯 Number Guessing - Logic and deduction")
    print("   🔤 Word Scramble - Language and pattern recognition")
    print("   🧮 Math Challenge - Mathematical problem solving")
    print("   🧩 Riddle Solving - Creative thinking and reasoning")
    print("   🐉 Final Boss - Combined skills challenge")
    print()
    
    print_separator()

def main():
    """Run the demo."""
    try:
        print_banner("MULTI-LEVEL CONSOLE GAME DEMO", width=80)
        print("🎮 This demo showcases the game's features and systems")
        print("🚀 To play the actual game, run: python main.py")
        print()
        
        demo_game_features()
        demo_player_system()
        demo_level_system()
        
        print_banner("DEMO COMPLETE", width=80)
        print("🎉 Demo completed successfully!")
        print("🎮 Ready to play the full game? Run: python main.py")
        print("📖 For more information, see README.md")
        
    except Exception as e:
        print_styled_text(f"Demo error: {e}", "error")

if __name__ == "__main__":
    main()
