# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing Demos!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
# Extensive Quantum Computing Code in Python

# Required Libraries
import cirq
import random

# Function to Demonstrate a Simple Quantum Circuit
def quantum_demo():
    # Create a qubit
    qubit = cirq.LineQubit(0)

    # Create a circuit with a Hadamard gate and measurement
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Put the qubit into superposition
        cirq.measure(qubit, key='result')  # Measure the qubit
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.histogram(key='result')

    print("\nSimple Quantum Circuit (Superposition):")
    print("Measurement Results:", dict(counts))

# Function to Demonstrate Quantum Entanglement
def quantum_entanglement():
    # Create two qubits
    qubits = cirq.LineQubit.range(2)

    # Create a circuit with a Hadamard and CNOT gate
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1]),  # Entangle the qubits
        cirq.measure(*qubits, key='result')  # Measure both qubits
    )

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Entanglement:")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Function to Demonstrate a Random Quantum Surprise
def quantum_surprise():
    # Randomly generate a number of qubits (1-3)
    num_qubits = random.randint(1, 3)
    qubits = cirq.LineQubit.range(num_qubits)

    # Randomly apply gates to each qubit
    operations = []
    for qubit in qubits:
        gate_choice = random.choice([cirq.H, cirq.X, cirq.Z])
        operations.append(gate_choice(qubit))

    # Add measurements
    operations.append(cirq.measure(*qubits, key='result'))

    # Create and simulate the circuit
    circuit = cirq.Circuit(operations)
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    counts = result.multi_measurement_histogram(keys=['result'])

    print("\nQuantum Surprise with", num_qubits, "qubit(s):")
    print("Measurement Results:", {tuple(k): v for k, v in counts.items()})

# Main Function
def main():
    print("Welcome to Quantum Computing!")

    # Run each quantum demonstration
    quantum_demo()
    quantum_entanglement()
    quantum_surprise()

if __name__ == "__main__":
    main()
