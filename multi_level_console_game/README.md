# Multi-Level Console Adventure Game 🎮

A comprehensive console-based adventure game featuring multiple levels with increasing difficulty. Test your skills in numbers, words, math, riddles, and face the ultimate challenge!

## 🌟 Features

- **5 Unique Levels**: Each with different challenge types and increasing difficulty
- **Progressive Gameplay**: Advance through levels by completing challenges
- **Lives System**: 3 lives with retry options for failed levels
- **Scoring System**: Earn points based on performance and speed
- **Achievement System**: Unlock achievements as you progress
- **Modern Console UI**: Clean, styled text with progress indicators
- **Comprehensive Statistics**: Track your performance across all levels
- **Replay Functionality**: Play again with reset statistics

## 🎯 Game Levels

### Level 1: Number Detective 🎯
- Guess a secret number between 1-100
- 7 attempts with hints (too high/too low)
- Score based on number of attempts

### Level 2: Word Unscrambler 🔤
- Unscramble 3 words related to adventure and computing
- 3 attempts per word with hints
- Complete by solving at least 2/3 words

### Level 3: Math Wizard 🧮
- Solve 5 mathematical problems with increasing difficulty
- Addition, subtraction, multiplication, division, and powers
- Complete by solving at least 3/5 problems

### Level 4: Riddle Master 🧩
- Solve 3 mind-bending riddles
- 2 attempts per riddle with hints
- Complete by solving at least 2/3 riddles

### Level 5: Ultimate Challenge 🐉
- Final boss battle combining all previous skills
- 3 mini-challenges: Speed Math, Memory Pattern, Ultimate Riddle
- Complete by succeeding in at least 2/3 challenges

## 🚀 How to Play

### Requirements
- Python 3.6 or higher
- Terminal/Console environment
- Keyboard for input

### Installation & Running

1. **Navigate to the game directory:**
   ```bash
   cd multi_level_console_game
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

3. **Alternative method:**
   ```bash
   python -m multi_level_console_game.main
   ```

### Game Controls
- Type your answers and press Enter
- For number inputs, enter digits only
- For yes/no questions, use 'y' or 'n'
- Press Ctrl+C at any time to quit
- Read questions carefully - some are case-sensitive

## 🎮 Gameplay Tips

- **Take your time** - Most challenges aren't timed (except the final boss)
- **Read carefully** - Some answers are simpler than they appear
- **Use hints** - They're provided when you make mistakes
- **Don't give up** - You can retry failed levels
- **Track progress** - Check your stats between levels

## 📊 Scoring System

- **Number Detective**: 10-100 points (based on attempts)
- **Word Unscrambler**: 10-30 points per word + bonus
- **Math Wizard**: 15-45 points per problem + bonus
- **Riddle Master**: 20-40 points per riddle + bonus
- **Ultimate Challenge**: 50-80 points per challenge + final bonus

## 🏅 Achievements

Unlock achievements by completing various challenges:
- **Number Detective** - Complete Level 1
- **Word Master** - Complete Level 2
- **Math Wizard** - Complete Level 3
- **Riddle Master** - Complete Level 4
- **Ultimate Champion** - Complete Level 5
- **Game Conqueror** - Complete all levels

## 📁 Project Structure

```
multi_level_console_game/
├── __init__.py          # Package initialization
├── main.py              # Entry point - run this file
├── game.py              # Main game controller
├── player.py            # Player state management
├── level.py             # Level definitions and challenges
├── utils.py             # Utility functions for UI and input
├── exceptions.py        # Custom game exceptions
└── README.md           # This file
```

## 🔧 Technical Details

### Architecture
- **Modular Design**: Separated concerns across multiple files
- **Object-Oriented**: Uses classes for Player, Game, and Level management
- **Error Handling**: Robust exception handling for user input and game errors
- **Type Hints**: Full type annotations for better code maintainability

### Key Classes
- `Game`: Main controller managing game flow and level progression
- `Player`: Manages player state, score, lives, and achievements
- `Level`: Base class for all game levels with specific implementations
- Various utility functions for UI, input validation, and formatting

### Error Handling
- Custom exceptions for different error types
- Graceful handling of invalid input
- Keyboard interrupt (Ctrl+C) support
- Automatic retry mechanisms for failed levels

## 🎨 UI Features

- **Styled Text**: Success, error, warning, and info messages with emojis
- **Progress Bars**: Visual representation of game progress
- **Banners**: Styled headers for different game sections
- **Separators**: Clean visual separation between game elements
- **Status Display**: Comprehensive player statistics

## 🐛 Troubleshooting

### Common Issues

1. **Python Version Error**
   - Ensure you have Python 3.6 or higher
   - Check with: `python --version`

2. **Import Errors**
   - Make sure you're running from the correct directory
   - Try: `python -m multi_level_console_game.main`

3. **Display Issues**
   - Ensure your terminal supports Unicode characters
   - Try running in a different terminal if characters don't display properly

4. **Input Problems**
   - Make sure you're in an interactive terminal environment
   - Some IDEs may not support interactive input properly

### Performance Tips
- The game is designed to run smoothly on any modern system
- If you experience lag, try running in a native terminal instead of an IDE
- Clear your terminal before starting for the best visual experience

## 🎯 Future Enhancements

Potential improvements for future versions:
- Save/load game progress
- Difficulty level selection
- More level types (logic puzzles, pattern recognition)
- Multiplayer support
- Sound effects (terminal beeps)
- Color support for compatible terminals
- Leaderboard system

## 📝 License

This game is created for educational and entertainment purposes. Feel free to modify and enhance it for your own use!

## 🤝 Contributing

This is a complete, self-contained game, but you can:
- Add new level types by extending the `Level` class
- Enhance the UI with additional styling
- Add new achievement types
- Improve the scoring system
- Add new utility functions

## 🎉 Enjoy the Game!

Have fun testing your skills across all five levels! Can you become the Ultimate Champion and conquer all challenges?

Good luck, adventurer! 🚀
