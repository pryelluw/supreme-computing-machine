from settings import GREETING, GOODBYE
from registry import app_registry


def app() -> None: 
    help = '\n'.join([f'{app} - {app_registry.app(app).help}' for app in app_registry.apps])    
    print(GREETING)

    while True:
        current_command = input("What would you like to do?  ")
        if current_command == "q":
            print(GOODBYE)
            break
        elif current_command == "h":
            print(f'\nCurrent available options:\n\n{help}\n')
        elif current_command in app_registry.apps:
            app_name = current_command
            # handover control to the app entry point
            # and return here when exits
            app_registry.app(app_name)['entry_point']()
        else:
            print('Invalid command my friend. Enter "h" to print help')
