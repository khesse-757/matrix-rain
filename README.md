# matrix-rain

Matrix letters rain down.

## Installation

```bash
pip install matrix-rain
```

Or from source:

```bash
git clone https://github.com/khesse-757/matrix-rain.git
cd matrix-rain
pip install -e .
```

## Usage

```python
from matrix_rain import YourClass

obj = YourClass()
result = obj.do_something()
```

## Development

```bash
# Clone the repository
git clone https://github.com/khesse-757/matrix-rain.git
cd matrix-rain

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install with dev dependencies
pip install -e .[dev]

# Run tests
pytest

# Check code quality
ruff check .
```

## License

MIT License - see LICENSE file for details.
