import sys
from pathlib import Path

# Add the flask-api root directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))
# Add the src directory to Python path for direct imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))