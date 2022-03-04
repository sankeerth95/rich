

#Simulatr take in a bunch of bets and simulate the output;
# derive type of simulator from under this class: Monte Carlo simulator, real data simulator, etc.
class SimulatorBase:
    def __init__(self, txns):
        pass

    def simulate(self):
        return NotImplementedError
