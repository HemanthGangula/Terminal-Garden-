import logging

class Plant:
    def __init__(self, stage=0, health=100):
        self.stage = max(stage, 0)
        self.health = max(health, 0)

    def grow(self):
        self.stage += 1
        print(f"Plant has grown to stage {self.stage}.")

    def water(self):
        self.health += 10
        print("Plant has been watered.")

    def status(self):
        print(f"Stage: {self.stage}, Health: {self.health}")

    def apply_weather_effect(self, weather):
        if weather == 'Sunny':
            self.health += 5
            print("Sunny weather! Your plant is thriving.")
        elif weather == 'Rainy':
            self.health += 10
            print("Rainy weather! Your plant is well-watered.")
        elif weather == 'Drought':
            self.health = max(self.health - 15, 0)
            print("Drought! Your plant is struggling.")
        elif weather == 'Storm':
            self.health = max(self.health - 20, 0)
            print("Stormy weather! Your plant has been damaged.")
        else:
            print("Unrecognized weather condition.")