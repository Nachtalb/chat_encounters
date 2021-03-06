import sys
from pathlib import Path

wrapper_module_path = Path(__file__).parent.absolute()
main_module_path = wrapper_module_path / 'chat_encounters'
module_str = str(wrapper_module_path)

# Module injection + cleanup of previous injection if need be
while module_str in sys.path:
    sys.path.remove(module_str)
sys.path.append(module_str)

for name, module in list(sys.modules.items())[:]:
    if name.startswith(main_module_path.name):
        sys.modules.pop(name)

from chat_encounters import Plugin

__all__ = ['Plugin']
