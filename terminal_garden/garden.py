import time
import threading
from terminal_garden.commands import CommandHandler
from terminal_garden.plant import Plant
from terminal_garden.weather import Weather
from terminal_garden.storage import Storage
from colorama import init, Fore, Style

init(autoreset=True)

def time_based_growth(plant, weather, storage):
    while True:
        time.sleep(60)  # Grow every 60 seconds
        plant.grow()
        current_weather = weather.generate_weather()
        plant.apply_weather_effect(current_weather)
        storage.save(plant)

def main():
    storage = Storage()
    saved_state = storage.load()
    if saved_state:
        plant = Plant(stage=saved_state.get('stage', 0), health=saved_state.get('health', 100))
    else:
        plant = Plant()
    weather = Weather()
    command_handler = CommandHandler(plant, weather, storage)

    growth_thread = threading.Thread(target=time_based_growth, args=(plant, weather, storage), daemon=True)
    growth_thread.start()

    print(Fore.GREEN + "Welcome to Terminal Garden!")
    while True:
        try:
            cmd = input(Fore.YELLOW + "Enter command: " + Style.RESET_ALL)
            command_handler.handle(cmd)
        except (KeyboardInterrupt, EOFError):
            print(Fore.RED + "\nExiting Terminal Garden. Goodbye!" + Style.RESET_ALL)
            storage.save(plant)
            break

if __name__ == "__main__":
    main()