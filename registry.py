class AppRegistry:
    def __init__(self):
        self.registry = {}
    
    def __call__(self):
        return self.registry
    
    def register(self, app_name: str, app_func: callable, app_help: str) -> None:
        self.registry[app_name] = {'help': app_help, 'func': app_func}
