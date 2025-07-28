"""
Player class to manage player state and progress.
"""

from typing import Dict, Any

class Player:
    """
    Represents a player in the game with their current state and progress.
    """
    
    def __init__(self, name: str = "Player"):
        """
        Initialize a new player.
        
        Args:
            name: The player's name
        """
        self.name = name
        self.current_level = 1
        self.score = 0
        self.health = 100
        self.lives = 3
        self.inventory = []
        self.achievements = []
        self.level_scores = {}  # Track score per level
        
    def update_score(self, points: int) -> None:
        """
        Update the player's score.
        
        Args:
            points: Points to add (can be negative)
        """
        self.score += points
        if self.score < 0:
            self.score = 0
    
    def advance_level(self) -> None:
        """
        Advance the player to the next level.
        """
        self.level_scores[self.current_level] = self.score
        self.current_level += 1
    
    def lose_life(self) -> bool:
        """
        Player loses a life.
        
        Returns:
            True if player still has lives, False if game over
        """
        self.lives -= 1
        return self.lives > 0
    
    def restore_health(self, amount: int = 20) -> None:
        """
        Restore player's health.
        
        Args:
            amount: Amount of health to restore
        """
        self.health += amount
        if self.health > 100:
            self.health = 100
    
    def take_damage(self, damage: int) -> bool:
        """
        Player takes damage.
        
        Args:
            damage: Amount of damage to take
            
        Returns:
            True if player is still alive, False if health reaches 0
        """
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return False
        return True
    
    def add_to_inventory(self, item: str) -> None:
        """
        Add an item to the player's inventory.
        
        Args:
            item: Item to add
        """
        if item not in self.inventory:
            self.inventory.append(item)
    
    def has_item(self, item: str) -> bool:
        """
        Check if player has a specific item.
        
        Args:
            item: Item to check for
            
        Returns:
            True if player has the item, False otherwise
        """
        return item in self.inventory
    
    def add_achievement(self, achievement: str) -> None:
        """
        Add an achievement to the player.
        
        Args:
            achievement: Achievement to add
        """
        if achievement not in self.achievements:
            self.achievements.append(achievement)
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get the current player status.
        
        Returns:
            Dictionary containing player status information
        """
        return {
            "name": self.name,
            "level": self.current_level,
            "score": self.score,
            "health": self.health,
            "lives": self.lives,
            "inventory_count": len(self.inventory),
            "achievements_count": len(self.achievements)
        }
    
    def display_status(self) -> None:
        """
        Display the player's current status in a formatted way.
        """
        print(f"\n📊 Player Status:")
        print(f"   Name: {self.name}")
        print(f"   Level: {self.current_level}")
        print(f"   Score: {self.score}")
        print(f"   Health: {self.health}/100")
        print(f"   Lives: {'❤️ ' * self.lives}")
        
        if self.inventory:
            print(f"   Inventory: {', '.join(self.inventory)}")
        
        if self.achievements:
            print(f"   Achievements: {len(self.achievements)} unlocked")
    
    def reset_for_new_game(self) -> None:
        """
        Reset player stats for a new game while keeping the name.
        """
        self.current_level = 1
        self.score = 0
        self.health = 100
        self.lives = 3
        self.inventory = []
        self.achievements = []
        self.level_scores = {}
