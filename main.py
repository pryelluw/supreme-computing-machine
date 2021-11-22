# !/usr/bin/env python3
from registry import AppRegistry

APP_NAME = '''
  _____ _    _ _____  _____  ______ __  __ ______    _____ ____  __  __ _____  _    _ _______ _____ _   _  _____   __  __          _____ _    _ _____ _   _ ______ 
 / ____| |  | |  __ \|  __ \|  ____|  \/  |  ____|  / ____/ __ \|  \/  |  __ \| |  | |__   __|_   _| \ | |/ ____| |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
| (___ | |  | | |__) | |__) | |__  | \  / | |__    | |   | |  | | \  / | |__) | |  | |  | |    | | |  \| | |  __  | \  / |  /  \ | |    | |__| | | | |  \| | |__   
 \___ \| |  | |  ___/|  _  /|  __| | |\/| |  __|   | |   | |  | | |\/| |  ___/| |  | |  | |    | | | . ` | | |_ | | |\/| | / /\ \| |    |  __  | | | | . ` |  __|  
 ____) | |__| | |    | | \ \| |____| |  | | |____  | |___| |__| | |  | | |    | |__| |  | |   _| |_| |\  | |__| | | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____ 
|_____/ \____/|_|    |_|  \_\______|_|  |_|______|  \_____\____/|_|  |_|_|     \____/   |_|  |_____|_| \_|\_____| |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______|
'''

GOODBYE = '\nGoodbye!\n'

def help(options: dict) -> str:
    return '\n'.join(options.keys())

def build_registry():
    registry = AppRegistry()
    registry.register('todo', help, 'hello help for todo')
    return registry



def main():
    print(APP_NAME)
    
    while True:
        registry = build_registry()
        print(registry.registry)
        current_command = input("What would you like to do?  ")
        
        if current_command == "q":
            print(GOODBYE)
            break
        
        elif current_command == "h":
            
            print(f'\nCurrent available options:\n{help(registry)}\n')
        
        else:
            print('Invalid command my friend. Enter "h" to print help')


if __name__ == '__main__':
    main()
