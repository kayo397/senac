class Device:
    def __init__(self, device_name):
        self._device_name = device_name

    def power_on(self):
        pass

class Printer(Device):
    def __init__(self, device_name):
        super().__init__(device_name)

    def power_on(self):
        return f"{self._device_name} is printing."

class Television(Device):
    def __init__(self, device_name):
        super().__init__(device_name)

    def power_on(self):
        return f"{self._device_name} is broadcasting a program."

class GameConsole(Device):
    def __init__(self, device_name):
        super().__init__(device_name)

    def power_on(self):
        return f"{self._device_name} is running a game."

class Drone(Device):
    def __init__(self, device_name):
        super().__init__(device_name)

    def power_on(self):
        return f"{self._device_name} is flying."

class AudioDevice(Device):
    def __init__(self, device_name):
        super().__init__(device_name)

    def power_on(self):
        return f"{self._device_name} is playing audio."

def show_power_on_status(devices):
    for device in devices:
        print(device.power_on())

devices = [Television("Samsung Smart TV"), Printer("Epson EcoTank"), GameConsole("Xbox Series X"), Drone("DJI Mavic Air"), AudioDevice("Bose SoundLink")]
show_power_on_status(devices)
