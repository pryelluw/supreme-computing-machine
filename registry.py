from typing import Callable, Any
from settings import INSTALLED_APPS

class AppRegistry:
    def __init__(self):
        self._registry = {}
    
    def register(self, app: Any) -> None:
        self._registry[app.name] = app
    
    @property
    def apps(self):
        return self._registry.keys()

    def app(self, app_name: str) -> Any:
        return self._registry[app_name]


def get_registry():
    registry = AppRegistry()
    for app in INSTALLED_APPS:
        registry.register(app)
    return registry

app_registry = get_registry()