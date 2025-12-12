"""
Tests for matrix rain module.
"""

from matrix_rain.matrix import MatrixRain, RainDrop


class TestRainDrop:
    """Test RainDrop class."""
    
    def test_create_raindrop(self):
        """Test raindrop creation."""
        drop = RainDrop(x=10, y=20, char="A", speed=1.0)
        assert drop.x == 10
        assert drop.y == 20
        assert drop.char == "A"
        assert drop.speed == 1.0
        assert drop.brightness == 1.0
    
    def test_update_raindrop(self):
        """Test raindrop update."""
        drop = RainDrop(x=10, y=20, char="A", speed=1.5)
        drop.update(height=100)
        assert drop.y == 21.5
        assert drop.brightness < 1.0


class TestMatrixRain:
    """Test MatrixRain class."""
    
    def test_create_matrix(self):
        """Test matrix creation."""
        matrix = MatrixRain(width=80, height=24)
        assert matrix.width == 80
        assert matrix.height == 24
        assert len(matrix.drops) > 0
    
    def test_update_matrix(self):
        """Test matrix update."""
        matrix = MatrixRain(width=80, height=24, density=0.1)
        initial_positions = [(d.x, d.y) for d in matrix.drops]
        matrix.update()
        updated_positions = [(d.x, d.y) for d in matrix.drops]
        assert initial_positions != updated_positions
    
    def test_get_frame(self):
        """Test getting frame."""
        matrix = MatrixRain(width=80, height=24)
        frame = matrix.get_frame()
        assert isinstance(frame, list)
        assert len(frame) == len(matrix.drops)