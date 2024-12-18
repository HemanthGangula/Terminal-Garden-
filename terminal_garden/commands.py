from terminal_garden.plant import Plant
from terminal_garden.weather import Weather
from terminal_garden.storage import Storage
from colorama import Fore, Style

class CommandHandler:
    def __init__(self, plant, weather, storage):
        self.plant = plant
        self.weather = weather
        self.storage = storage

    def handle(self, command):
        if command.lower() == 'plant seed':
            self.plant = Plant()
            print(Fore.GREEN + "A new seed has been planted." + Style.RESET_ALL)
            self.storage.save(self.plant)
        elif command.lower() == 'water':
            self.plant.water()
            self.storage.save(self.plant)
        elif command.lower() == 'status':
            self.plant.status()
        elif command.lower() == 'weather':
            current_weather = self.weather.generate_weather()
            print(Fore.CYAN + f"Weather Event: {current_weather}" + Style.RESET_ALL)
        elif command.lower() == 'save':
            self.storage.save(self.plant)
        elif command.lower() == 'load':
            saved_state = self.storage.load()
            if saved_state:
                self.plant.stage = saved_state.get('stage', self.plant.stage)
                self.plant.health = saved_state.get('health', self.plant.health)
                print(Fore.GREEN + "Garden state has been loaded." + Style.RESET_ALL)
        elif command.lower() == 'reset':
            confirm = input(Fore.RED + "Are you sure you want to reset your garden? This will delete the current state. (yes/no): " + Style.RESET_ALL)
            if confirm.lower() == 'yes':
                self.plant.stage = 0
                self.plant.health = 100
                self.storage.save(self.plant)
                print(Fore.GREEN + "Garden has been reset." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "Reset canceled." + Style.RESET_ALL)
        elif command.lower() == 'help':
            self.display_help()
        elif command.lower() == 'exit':
            print(Fore.RED + "Exiting Terminal Garden. Goodbye!" + Style.RESET_ALL)
            self.storage.save(self.plant)
            exit(0)
        else:
            print(Fore.RED + "Unknown command. Type 'help' to see available commands." + Style.RESET_ALL)

    def display_help(self):
        help_text = f"""
{Fore.MAGENTA}Available Commands:{Style.RESET_ALL}
  {Fore.GREEN}plant seed{Style.RESET_ALL}  - Start your garden by planting a seed.
  {Fore.GREEN}water{Style.RESET_ALL}       - Water your plant to improve its health.
  {Fore.GREEN}status{Style.RESET_ALL}      - Check the current status of your plant.
  {Fore.GREEN}weather{Style.RESET_ALL}     - View the current weather event.
  {Fore.GREEN}save{Style.RESET_ALL}        - Manually save the current garden state.
  {Fore.GREEN}load{Style.RESET_ALL}        - Load the garden state from the saved file.
  {Fore.GREEN}reset{Style.RESET_ALL}       - Reset your garden to its initial state.
  {Fore.GREEN}help{Style.RESET_ALL}        - Display this help message.
  {Fore.GREEN}exit{Style.RESET_ALL}        - Exit the Terminal Garden application.
        """
        print(help_text)