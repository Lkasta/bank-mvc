import sys
from pathlib import Path

# Adiciona a raiz do projeto ao sys.path para o pytest
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
