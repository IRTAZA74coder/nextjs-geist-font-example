"""
Level classes and individual level challenges for the multi-level console game.
"""

import random
import time
from typing import List, Dict, Any
from utils import print_banner, print_separator, get_input, print_styled_text
from exceptions import LevelError, GameOverError
from player import Player

class Level:
    """
    Base class for game levels.
    """
    
    def __init__(self, level_number: int, title: str, description: str):
        """
        Initialize a level.
        
        Args:
            level_number: The level number
            title: Title of the level
            description: Description of the level challenge
        """
        self.level_number = level_number
        self.title = title
        self.description = description
        self.max_score = 100
        self.time_limit = None  # No time limit by default
    
    def play_level(self, player: Player) -> bool:
        """
        Play the level. To be implemented by subclasses.
        
        Args:
            player: The player object
            
        Returns:
            True if level completed successfully, False otherwise
        """
        raise NotImplementedError("Subclasses must implement play_level method")
    
    def display_intro(self) -> None:
        """
        Display the level introduction.
        """
        print_banner(f"LEVEL {self.level_number}: {self.title}")
        print(f"📝 {self.description}\n")
        print_separator()

class NumberGuessingLevel(Level):
    """
    Level 1: Number Guessing Game
    """
    
    def __init__(self):
        super().__init__(
            level_number=1,
            title="Number Detective",
            description="I'm thinking of a number between 1 and 100. Can you guess it?"
        )
        self.max_attempts = 7
    
    def play_level(self, player: Player) -> bool:
        """
        Play the number guessing level.
        """
        self.display_intro()
        
        secret_number = random.randint(1, 100)
        attempts = 0
        
        print(f"🎯 You have {self.max_attempts} attempts to guess the number!")
        print("💡 Hint: I'll tell you if your guess is too high or too low.\n")
        
        while attempts < self.max_attempts:
            attempts += 1
            remaining = self.max_attempts - attempts + 1
            
            try:
                guess = get_input(f"Attempt {attempts}/{self.max_attempts} - Enter your guess (1-100)", input_type="int")
                
                if guess < 1 or guess > 100:
                    print_styled_text("Please guess a number between 1 and 100!", "warning")
                    attempts -= 1  # Don't count invalid guesses
                    continue
                
                if guess == secret_number:
                    score = max(10, 100 - (attempts - 1) * 10)
                    player.update_score(score)
                    print_styled_text(f"🎉 Congratulations! You guessed it in {attempts} attempts!", "success")
                    print_styled_text(f"You earned {score} points!", "success")
                    player.add_achievement("Number Detective")
                    return True
                
                elif guess < secret_number:
                    print_styled_text(f"📈 Too low! {remaining} attempts remaining.", "info")
                else:
                    print_styled_text(f"📉 Too high! {remaining} attempts remaining.", "info")
                    
            except Exception as e:
                raise LevelError(f"Error in number guessing level: {e}")
        
        print_styled_text(f"💔 Game Over! The number was {secret_number}.", "error")
        player.lose_life()
        return False

class WordScrambleLevel(Level):
    """
    Level 2: Word Scramble Challenge
    """
    
    def __init__(self):
        super().__init__(
            level_number=2,
            title="Word Unscrambler",
            description="Unscramble the letters to form valid words!"
        )
        self.words = [
            "PYTHON", "COMPUTER", "CHALLENGE", "ADVENTURE", "MYSTERY",
            "TREASURE", "JOURNEY", "DISCOVERY", "PUZZLE", "VICTORY"
        ]
    
    def scramble_word(self, word: str) -> str:
        """
        Scramble the letters of a word.
        """
        letters = list(word)
        random.shuffle(letters)
        return ''.join(letters)
    
    def play_level(self, player: Player) -> bool:
        """
        Play the word scramble level.
        """
        self.display_intro()
        
        words_to_solve = random.sample(self.words, 3)
        solved_count = 0
        
        print("🔤 Unscramble these 3 words to complete the level!")
        print("💡 Hint: All words are related to adventure and computing.\n")
        
        for i, word in enumerate(words_to_solve, 1):
            scrambled = self.scramble_word(word)
            
            # Make sure scrambled word is different from original
            while scrambled == word:
                scrambled = self.scramble_word(word)
            
            print(f"Word {i}/3: {scrambled}")
            print(f"Letters: {len(word)} | Hint: {word[0]}___")
            
            attempts = 0
            max_attempts = 3
            
            while attempts < max_attempts:
                attempts += 1
                guess = get_input(f"Your answer (attempt {attempts}/{max_attempts})").upper()
                
                if guess == word:
                    score = max(10, 30 - (attempts - 1) * 5)
                    player.update_score(score)
                    print_styled_text(f"✅ Correct! '{word}' (+{score} points)", "success")
                    solved_count += 1
                    break
                else:
                    if attempts < max_attempts:
                        print_styled_text(f"❌ Incorrect. Try again!", "error")
                    else:
                        print_styled_text(f"❌ The word was '{word}'", "error")
            
            print()
        
        if solved_count >= 2:
            bonus = solved_count * 10
            player.update_score(bonus)
            print_styled_text(f"🎉 Level Complete! You solved {solved_count}/3 words!", "success")
            print_styled_text(f"Bonus: +{bonus} points!", "success")
            player.add_achievement("Word Master")
            return True
        else:
            print_styled_text(f"💔 Level Failed. You only solved {solved_count}/3 words.", "error")
            player.lose_life()
            return False

class MathChallengeLevel(Level):
    """
    Level 3: Math Challenge
    """
    
    def __init__(self):
        super().__init__(
            level_number=3,
            title="Math Wizard",
            description="Solve mathematical problems to prove your skills!"
        )
    
    def generate_problem(self, difficulty: int) -> tuple:
        """
        Generate a math problem based on difficulty.
        
        Returns:
            Tuple of (problem_string, correct_answer)
        """
        if difficulty == 1:
            a, b = random.randint(1, 20), random.randint(1, 20)
            operation = random.choice(['+', '-'])
            if operation == '+':
                return f"{a} + {b}", a + b
            else:
                return f"{a} - {b}", a - b
        
        elif difficulty == 2:
            a, b = random.randint(2, 12), random.randint(2, 12)
            operation = random.choice(['*', '/'])
            if operation == '*':
                return f"{a} × {b}", a * b
            else:
                result = a * b
                return f"{result} ÷ {a}", b
        
        else:  # difficulty == 3
            a, b = random.randint(1, 10), random.randint(2, 4)
            return f"{a}^{b}", a ** b
    
    def play_level(self, player: Player) -> bool:
        """
        Play the math challenge level.
        """
        self.display_intro()
        
        problems_solved = 0
        total_problems = 5
        
        print(f"🧮 Solve {total_problems} math problems!")
        print("💡 Problems get harder as you progress.\n")
        
        for i in range(1, total_problems + 1):
            difficulty = min(3, (i + 1) // 2)  # Gradually increase difficulty
            problem, answer = self.generate_problem(difficulty)
            
            print(f"Problem {i}/{total_problems} (Difficulty: {'⭐' * difficulty})")
            print(f"Calculate: {problem}")
            
            try:
                user_answer = get_input("Your answer", input_type="int")
                
                if user_answer == answer:
                    score = difficulty * 15
                    player.update_score(score)
                    print_styled_text(f"✅ Correct! (+{score} points)", "success")
                    problems_solved += 1
                else:
                    print_styled_text(f"❌ Wrong! The answer was {answer}", "error")
                
            except Exception as e:
                print_styled_text(f"❌ Invalid input! The answer was {answer}", "error")
            
            print()
        
        if problems_solved >= 3:
            bonus = problems_solved * 10
            player.update_score(bonus)
            print_styled_text(f"🎉 Level Complete! You solved {problems_solved}/{total_problems} problems!", "success")
            print_styled_text(f"Bonus: +{bonus} points!", "success")
            player.add_achievement("Math Wizard")
            return True
        else:
            print_styled_text(f"💔 Level Failed. You only solved {problems_solved}/{total_problems} problems.", "error")
            player.lose_life()
            return False

class RiddleLevel(Level):
    """
    Level 4: Riddle Challenge
    """
    
    def __init__(self):
        super().__init__(
            level_number=4,
            title="Riddle Master",
            description="Solve these mind-bending riddles!"
        )
        self.riddles = [
            {
                "question": "I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?",
                "answer": "keyboard",
                "hint": "You're using one right now to play this game!"
            },
            {
                "question": "The more you take, the more you leave behind. What am I?",
                "answer": "footsteps",
                "hint": "Think about walking..."
            },
            {
                "question": "I'm tall when I'm young, and short when I'm old. What am I?",
                "answer": "candle",
                "hint": "I provide light and melt away..."
            },
            {
                "question": "What has hands but cannot clap?",
                "answer": "clock",
                "hint": "It tells you something important every day..."
            },
            {
                "question": "I have a head and a tail, but no body. What am I?",
                "answer": "coin",
                "hint": "You might flip me to make a decision..."
            }
        ]
    
    def play_level(self, player: Player) -> bool:
        """
        Play the riddle level.
        """
        self.display_intro()
        
        riddles_to_solve = random.sample(self.riddles, 3)
        solved_count = 0
        
        print("🧩 Solve these 3 riddles to complete the level!")
        print("💡 Think carefully - the answers might be simpler than you think.\n")
        
        for i, riddle in enumerate(riddles_to_solve, 1):
            print(f"Riddle {i}/3:")
            print(f"❓ {riddle['question']}")
            
            attempts = 0
            max_attempts = 2
            
            while attempts < max_attempts:
                attempts += 1
                answer = get_input(f"Your answer (attempt {attempts}/{max_attempts})").lower().strip()
                
                if answer == riddle['answer']:
                    score = max(20, 40 - (attempts - 1) * 10)
                    player.update_score(score)
                    print_styled_text(f"🎯 Excellent! The answer is '{riddle['answer']}'! (+{score} points)", "success")
                    solved_count += 1
                    break
                else:
                    if attempts < max_attempts:
                        print_styled_text(f"🤔 Not quite right. Hint: {riddle['hint']}", "warning")
                    else:
                        print_styled_text(f"❌ The answer was '{riddle['answer']}'", "error")
            
            print()
        
        if solved_count >= 2:
            bonus = solved_count * 15
            player.update_score(bonus)
            print_styled_text(f"🎉 Level Complete! You solved {solved_count}/3 riddles!", "success")
            print_styled_text(f"Bonus: +{bonus} points!", "success")
            player.add_achievement("Riddle Master")
            return True
        else:
            print_styled_text(f"💔 Level Failed. You only solved {solved_count}/3 riddles.", "error")
            player.lose_life()
            return False

class FinalBossLevel(Level):
    """
    Level 5: Final Boss Challenge
    """
    
    def __init__(self):
        super().__init__(
            level_number=5,
            title="The Ultimate Challenge",
            description="Face the final boss in this ultimate test of all your skills!"
        )
    
    def play_level(self, player: Player) -> bool:
        """
        Play the final boss level - combines elements from all previous levels.
        """
        self.display_intro()
        
        print("🐉 You face the Ultimate Challenge!")
        print("🎯 Complete 3 different mini-challenges to defeat the boss!")
        print("⚠️  This is your final test - use all the skills you've learned!\n")
        
        challenges_completed = 0
        total_challenges = 3
        
        # Challenge 1: Speed Math
        print("🔥 BOSS CHALLENGE 1: Speed Math")
        print("Solve 3 math problems quickly!")
        
        start_time = time.time()
        math_correct = 0
        
        for i in range(3):
            a, b = random.randint(1, 15), random.randint(1, 15)
            operation = random.choice(['+', '-', '*'])
            
            if operation == '+':
                problem, answer = f"{a} + {b}", a + b
            elif operation == '-':
                problem, answer = f"{a} - {b}", a - b
            else:
                problem, answer = f"{a} × {b}", a * b
            
            try:
                user_answer = get_input(f"Quick! {problem} =", input_type="int")
                if user_answer == answer:
                    math_correct += 1
                    print_styled_text("✅ Correct!", "success")
                else:
                    print_styled_text(f"❌ Wrong! Answer was {answer}", "error")
            except:
                print_styled_text(f"❌ Invalid! Answer was {answer}", "error")
        
        elapsed_time = time.time() - start_time
        
        if math_correct >= 2 and elapsed_time <= 30:
            challenges_completed += 1
            score = 50 + max(0, int(30 - elapsed_time))
            player.update_score(score)
            print_styled_text(f"🎉 Challenge 1 Complete! Time: {elapsed_time:.1f}s (+{score} points)", "success")
        else:
            print_styled_text("💔 Challenge 1 Failed!", "error")
        
        print()
        
        # Challenge 2: Memory Pattern
        print("🔥 BOSS CHALLENGE 2: Memory Pattern")
        print("Remember and repeat this sequence!")
        
        sequence = [random.randint(1, 4) for _ in range(5)]
        sequence_str = ' '.join(map(str, sequence))
        
        print(f"Memorize this: {sequence_str}")
        time.sleep(3)
        print("\n" * 10)  # Clear the sequence from view
        
        try:
            user_sequence = get_input("Enter the sequence (numbers separated by spaces)")
            user_numbers = [int(x) for x in user_sequence.split()]
            
            if user_numbers == sequence:
                challenges_completed += 1
                player.update_score(60)
                print_styled_text("🎉 Challenge 2 Complete! Perfect memory! (+60 points)", "success")
            else:
                print_styled_text(f"❌ Wrong sequence! It was: {sequence_str}", "error")
        except:
            print_styled_text(f"❌ Invalid input! Sequence was: {sequence_str}", "error")
        
        print()
        
        # Challenge 3: Final Riddle
        print("🔥 BOSS CHALLENGE 3: The Ultimate Riddle")
        final_riddle = {
            "question": "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
            "answer": "fire",
            "hint": "I'm hot and bright, and I dance in the wind..."
        }
        
        print(f"❓ {final_riddle['question']}")
        
        attempts = 0
        max_attempts = 2
        
        while attempts < max_attempts:
            attempts += 1
            answer = get_input(f"Your final answer (attempt {attempts}/{max_attempts})").lower().strip()
            
            if answer == final_riddle['answer']:
                challenges_completed += 1
                player.update_score(80)
                print_styled_text("🎉 Challenge 3 Complete! You solved the ultimate riddle! (+80 points)", "success")
                break
            else:
                if attempts < max_attempts:
                    print_styled_text(f"🤔 Think harder... Hint: {final_riddle['hint']}", "warning")
                else:
                    print_styled_text(f"❌ The answer was '{final_riddle['answer']}'", "error")
        
        print()
        print_separator()
        
        # Final Results
        if challenges_completed >= 2:
            final_bonus = challenges_completed * 50
            player.update_score(final_bonus)
            print_styled_text("🏆 CONGRATULATIONS! YOU HAVE DEFEATED THE ULTIMATE CHALLENGE!", "success")
            print_styled_text(f"Challenges completed: {challenges_completed}/3", "success")
            print_styled_text(f"Final bonus: +{final_bonus} points!", "success")
            player.add_achievement("Ultimate Champion")
            player.add_achievement("Game Conqueror")
            return True
        else:
            print_styled_text(f"💔 The boss was too strong! You completed {challenges_completed}/3 challenges.", "error")
            print_styled_text("But you fought bravely! Try again to claim victory!", "info")
            player.lose_life()
            return False

# Level registry - easy way to access all levels
LEVELS = [
    NumberGuessingLevel(),
    WordScrambleLevel(),
    MathChallengeLevel(),
    RiddleLevel(),
    FinalBossLevel()
]

def get_level(level_number: int) -> Level:
    """
    Get a level by its number.
    
    Args:
        level_number: The level number to retrieve
        
    Returns:
        The level object
        
    Raises:
        LevelError: If level number is invalid
    """
    if 1 <= level_number <= len(LEVELS):
        return LEVELS[level_number - 1]
    else:
        raise LevelError(f"Invalid level number: {level_number}")
