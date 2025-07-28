"""
Core game logic and level management for the multi-level console game.
"""

import time
from typing import Optional
from player import Player
from level import LEVELS, get_level
from utils import (
    print_banner, print_separator, get_input, print_styled_text, 
    clear_screen, display_progress_bar
)
from exceptions import LevelError, GameOverError

class Game:
    """
    Main game controller that manages game flow and level progression.
    """
    
    def __init__(self):
        """
        Initialize the game.
        """
        self.player: Optional[Player] = None
        self.current_level = 1
        self.max_level = len(LEVELS)
        self.game_completed = False
        self.start_time = None
        
    def initialize_player(self) -> None:
        """
        Initialize the player with their name and starting stats.
        """
        print_banner("WELCOME TO THE ULTIMATE ADVENTURE!")
        print("🎮 Prepare yourself for an epic multi-level challenge!")
        print("🌟 Test your skills in numbers, words, math, riddles, and more!")
        print("💪 Each level gets progressively harder - do you have what it takes?\n")
        
        print_separator()
        print("📋 GAME RULES:")
        print("   • Complete each level to advance to the next")
        print("   • You have 3 lives - lose them all and it's game over!")
        print("   • Earn points for correct answers and quick thinking")
        print("   • Unlock achievements as you progress")
        print("   • Face the Ultimate Challenge in the final level!")
        print_separator()
        
        name = get_input("\n👤 Enter your adventurer name (or press Enter for 'Hero')")
        if not name.strip():
            name = "Hero"
        
        self.player = Player(name)
        print_styled_text(f"Welcome, {self.player.name}! Your adventure begins now!", "success")
        
        # Ask if player wants to see controls
        show_controls = get_input("Would you like to see the game controls? (y/n)", 
                                 valid_options=['y', 'n', 'yes', 'no'])
        
        if show_controls in ['y', 'yes']:
            self.show_controls()
        
        input("\nPress Enter to begin your adventure...")
        clear_screen()
    
    def show_controls(self) -> None:
        """
        Display game controls and tips.
        """
        print("\n🎮 GAME CONTROLS & TIPS:")
        print("   • Type your answers and press Enter")
        print("   • For number inputs, enter digits only")
        print("   • For yes/no questions, use 'y' or 'n'")
        print("   • Press Ctrl+C at any time to quit")
        print("   • Read questions carefully - some are case-sensitive")
        print("   • Take your time, but some challenges are timed!")
        print("   • Your progress is saved between levels")
    
    def display_game_status(self) -> None:
        """
        Display current game status and progress.
        """
        print_separator()
        self.player.display_status()
        
        # Show progress bar
        progress = (self.current_level - 1) / self.max_level
        display_progress_bar(self.current_level - 1, self.max_level, 40)
        
        print(f"🎯 Current Objective: Complete Level {self.current_level}")
        print_separator()
    
    def play_level(self, level_number: int) -> bool:
        """
        Play a specific level.
        
        Args:
            level_number: The level number to play
            
        Returns:
            True if level completed successfully, False otherwise
        """
        try:
            level = get_level(level_number)
            
            # Show level intro with dramatic pause
            print(f"\n🚀 Preparing Level {level_number}...")
            time.sleep(1)
            clear_screen()
            
            # Play the level
            success = level.play_level(self.player)
            
            if success:
                print_styled_text(f"🎉 Level {level_number} Complete!", "success")
                self.player.advance_level()
                
                # Show level completion stats
                print(f"\n📊 Level {level_number} Results:")
                print(f"   Status: ✅ COMPLETED")
                print(f"   Current Score: {self.player.score}")
                print(f"   Lives Remaining: {'❤️ ' * self.player.lives}")
                
                if level_number < self.max_level:
                    print_styled_text(f"Get ready for Level {level_number + 1}!", "info")
                    input("\nPress Enter to continue...")
                    clear_screen()
                else:
                    self.game_completed = True
                    
                return True
            else:
                print_styled_text(f"💔 Level {level_number} Failed!", "error")
                
                if self.player.lives <= 0:
                    raise GameOverError("No lives remaining!")
                
                # Ask if player wants to retry
                retry = get_input("Would you like to retry this level? (y/n)", 
                                valid_options=['y', 'n', 'yes', 'no'])
                
                if retry in ['y', 'yes']:
                    print_styled_text("🔄 Retrying level...", "info")
                    time.sleep(1)
                    return self.play_level(level_number)  # Recursive retry
                else:
                    return False
                    
        except LevelError as e:
            print_styled_text(f"Level Error: {e}", "error")
            return False
        except Exception as e:
            print_styled_text(f"Unexpected error in level {level_number}: {e}", "error")
            return False
    
    def show_final_results(self) -> None:
        """
        Display final game results and statistics.
        """
        clear_screen()
        
        if self.game_completed:
            print_banner("🏆 VICTORY! GAME COMPLETED! 🏆")
            print_styled_text("Congratulations! You have conquered all challenges!", "success")
        else:
            print_banner("💔 GAME OVER")
            print_styled_text("Your adventure ends here, but you fought bravely!", "info")
        
        # Calculate total game time
        if self.start_time:
            total_time = time.time() - self.start_time
            minutes = int(total_time // 60)
            seconds = int(total_time % 60)
            time_str = f"{minutes}m {seconds}s" if minutes > 0 else f"{seconds}s"
        else:
            time_str = "Unknown"
        
        # Display comprehensive stats
        print("\n📊 FINAL STATISTICS:")
        print(f"   Player: {self.player.name}")
        print(f"   Levels Completed: {self.current_level - 1}/{self.max_level}")
        print(f"   Final Score: {self.player.score}")
        print(f"   Lives Used: {3 - self.player.lives}/3")
        print(f"   Total Play Time: {time_str}")
        print(f"   Achievements Unlocked: {len(self.player.achievements)}")
        
        if self.player.achievements:
            print(f"\n🏅 ACHIEVEMENTS EARNED:")
            for achievement in self.player.achievements:
                print(f"   ⭐ {achievement}")
        
        # Performance rating
        completion_rate = (self.current_level - 1) / self.max_level
        if completion_rate == 1.0:
            rating = "🏆 LEGENDARY CHAMPION"
        elif completion_rate >= 0.8:
            rating = "🥇 MASTER ADVENTURER"
        elif completion_rate >= 0.6:
            rating = "🥈 SKILLED EXPLORER"
        elif completion_rate >= 0.4:
            rating = "🥉 BRAVE WARRIOR"
        else:
            rating = "🌟 DETERMINED BEGINNER"
        
        print(f"\n🎖️  FINAL RATING: {rating}")
        
        # Score breakdown
        if self.player.level_scores:
            print(f"\n📈 SCORE BREAKDOWN:")
            for level, score in self.player.level_scores.items():
                print(f"   Level {level}: {score} points")
        
        print_separator()
    
    def ask_play_again(self) -> bool:
        """
        Ask if the player wants to play again.
        
        Returns:
            True if player wants to play again, False otherwise
        """
        play_again = get_input("Would you like to play again? (y/n)", 
                              valid_options=['y', 'n', 'yes', 'no'])
        
        return play_again in ['y', 'yes']
    
    def reset_game(self) -> None:
        """
        Reset the game for a new playthrough.
        """
        if self.player:
            name = self.player.name  # Keep the same name
            self.player.reset_for_new_game()
        
        self.current_level = 1
        self.game_completed = False
        self.start_time = None
        
        print_styled_text("🔄 Game reset! Starting new adventure...", "info")
        time.sleep(1)
        clear_screen()
    
    def run_game(self) -> None:
        """
        Main game loop - orchestrates the entire game experience.
        """
        try:
            while True:  # Main game loop for replaying
                # Initialize player if not already done
                if not self.player:
                    self.initialize_player()
                
                self.start_time = time.time()
                self.current_level = 1
                
                # Main level progression loop
                while self.current_level <= self.max_level and not self.game_completed:
                    try:
                        # Display current status
                        self.display_game_status()
                        
                        # Play the current level
                        if self.play_level(self.current_level):
                            self.current_level += 1
                        else:
                            # Level failed and player chose not to retry
                            break
                            
                    except GameOverError:
                        print_styled_text("💀 GAME OVER - No lives remaining!", "error")
                        break
                    except KeyboardInterrupt:
                        print_styled_text("\n\n👋 Game interrupted by player. Thanks for playing!", "info")
                        return
                    except Exception as e:
                        print_styled_text(f"Unexpected error: {e}", "error")
                        print_styled_text("The game will continue...", "info")
                        time.sleep(2)
                
                # Show final results
                self.show_final_results()
                
                # Ask if player wants to play again
                if self.ask_play_again():
                    self.reset_game()
                else:
                    break
            
            # Final goodbye message
            print_banner("THANKS FOR PLAYING!")
            print("🌟 Thank you for embarking on this adventure!")
            print("🎮 Come back anytime to test your skills again!")
            print("💫 Remember: every expert was once a beginner!")
            
        except KeyboardInterrupt:
            print_styled_text("\n\n👋 Thanks for playing! See you next time!", "info")
        except Exception as e:
            print_styled_text(f"Fatal error: {e}", "error")
            print_styled_text("The game will now exit.", "error")
