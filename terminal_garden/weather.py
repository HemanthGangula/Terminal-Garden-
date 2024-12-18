import random

class Weather:
    """
    Handles weather events affecting the plant.
    """
    def __init__(self):
        self.current_weather = None

    def generate_weather(self):
        """
        Randomly selects a weather condition.
        """
        weather_conditions = ['Sunny', 'Rainy', 'Drought', 'Storm']
        self.current_weather = random.choice(weather_conditions)
        print(f"Weather Event: {self.current_weather}")
        return self.current_weather

    def get_current_weather(self):
        """
        Returns the current weather condition.
        """
        return self.current_weather