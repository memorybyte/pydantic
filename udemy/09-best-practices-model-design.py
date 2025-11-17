from typing import Optional
from pydantic import BaseModel

# Model Organization:
# 1. Define leaf models first - Model with no dependencies
# 2. Build upward - Gradually compose more complex models
# 3. Use clear naming - Make relationships obvious
# 4. Group related models - keep model