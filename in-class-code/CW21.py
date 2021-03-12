class LightBulb:
    # Whether its on or off = state
    # state is a boolean, true = on, false = off

    # Constructor
    def __init__(self, state):
        self.state = state  # <-- Field

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def print_state(self):
        if self.state:
            print("ON")
        else:
            print("OFF")


# light_bulb1 = LightBulb(False)
# light_bulb1.print_state()
# light_bulb1.turn_on()
# light_bulb1.print_state()

light_bulbs = [LightBulb(False), LightBulb(True), LightBulb(False)]

for i in light_bulbs:
    if i.state == False:
        i.turn_on()
    i.print_state()
