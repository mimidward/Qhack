import sys
import pennylane as qml
from pennylane import numpy as np


def deutsch_jozsa(oracle):
    """This function will determine whether an oracle defined by a function f is constant or balanced.

    Args:
        - oracle (function): Encoding of the f function as a quantum gate. The first two qubits refer to the input and the third to the output.

    Returns:
        - (str): "constant" or "balanced"
    """

    dev = qml.device("default.qubit", wires=3, shots=1)

    @qml.qnode(dev)
    def circuit():
        """Implements the Deutsch Jozsa algorithm."""

        # QHACK #

        # Insert any pre-oracle processing here
        def blackbox_fuction():
            def f1(x):
                return 0
            def f2(x):
                return 1
            def f3(x):
                return x
            def f4(x):
                if x == 0:
                    return 1
                else:
                    return 0
            

        oracle()  # DO NOT MODIFY this line

        # Insert any post-oracle processing here
        sample = sys.stdin.read().split(",")        

        # QHACK #

        return qml.sample(wires=range(2))

    sample = circuit()

    # QHACK #

    # From `sample` (a single call to the circuit), determine whether the function is constant or balanced.
    if sample(0) == sample(1):
        return "constant"
    else:
        return "balanced"

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    numbers = [int(i) for i in inputs]

    def oracle():
        for i in numbers:
            qml.CNOT(wires=[i, 2])

    output = deutsch_jozsa(oracle)
    print(output)
