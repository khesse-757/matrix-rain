"""
Matrix rain effect generator.
"""

import random
import string
from dataclasses import dataclass
from typing import List


@dataclass
class RainDrop:
    """Represents a single character drop in the matrix rain."""
    
    x: int
    y: int
    char: str
    speed: float
    brightness: float = 1.0
    
    def update(self, height: int):
        """Update the raindrop position."""
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.brightness = 1.0
        else:
            self.brightness *= 0.98


class MatrixRain:
    """Matrix rain effect generator."""
    
    def __init__(self, width: int, height: int, density: float = 0.05):
        """
        Initialize the matrix rain.
        
        Args:
            width: Width of the canvas
            height: Height of the canvas
            density: Drop density (0.0 to 1.0)
        """
        self.width = width
        self.height = height
        self.density = density
        self.drops: List[RainDrop] = []
        self.characters = string.ascii_letters + string.digits + "!@#$%^&*()"
        
        self._initialize_drops()
    
    def _initialize_drops(self):
        """Create initial raindrops."""
        num_drops = int(self.width * self.density)
        for _ in range(num_drops):
            drop = RainDrop(
                x=random.randint(0, self.width - 1),
                y=random.randint(0, self.height - 1),
                char=random.choice(self.characters),
                speed=random.uniform(0.5, 2.0)
            )
            self.drops.append(drop)
    
    def update(self):
        """Update all raindrops."""
        for drop in self.drops:
            drop.update(self.height)
            drop.char = random.choice(self.characters)
    
    def get_frame(self) -> List[RainDrop]:
        """Get current frame of raindrops."""
        return self.drops.copy()