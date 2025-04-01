from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Receiver: Light
class Light:
    def on(self):
        print("The light is ON.")

    def off(self):
        print("The light is OFF.")


# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# Concrete Command
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# Receiver: Fan
class Fan:
    def start(self):
        print("The fan is ON.")

    def stop(self):
        print("The fan is OFF.")


# Concrete Command
class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.start()

    def undo(self):
        self.fan.stop()


# Concrete Command
class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.stop()

    def undo(self):
        self.fan.start()


# Receiver: Air Conditioner
class AirConditioner:
    def start_cooling(self):
        print("The air conditioner is cooling the room.")

    def stop_cooling(self):
        print("The air conditioner is stopped.")


# Concrete Command
class ACOnCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.start_cooling()

    def undo(self):
        self.ac.stop_cooling()


# Concrete Command
class ACOffCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.stop_cooling()

    def undo(self):
        self.ac.start_cooling()


# Invoker
class SmartHomeController:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("No commands to undo.")


# Client Code
def main():
    light = Light()
    fan = Fan()
    ac = AirConditioner()

    light_on = LightOnCommand(light)
    fan_on = FanOnCommand(fan)
    ac_on = ACOnCommand(ac)

    # light_off = LightOffCommand(light)
    # fan_off = FanOffCommand(fan)
    # ac_off = ACOffCommand(ac)

    controller = SmartHomeController()

    print("\nTurning ON the light:")
    controller.execute_command(light_on)

    print("\nTurning ON the fan:")
    controller.execute_command(fan_on)

    print("\nTurning ON the air conditioner:")
    controller.execute_command(ac_on)

    # Undo دستورات
    print("\nUndo last command (air conditioner):")
    controller.undo_last_command()

    print("\nUndo last command (fan):")
    controller.undo_last_command()

    print("\nUndo last command (light):")
    controller.undo_last_command()


if __name__ == "__main__":
    main()
