from azure.quantum.cirq import AzureQuantumService
service = AzureQuantumService(
    resource_id="",
    location="West US",
    default_target="ionq.simulator"
)

# Import Cirq and Numpy
import cirq
import numpy as np

# create two qubit circuit
q0, q1 = cirq.LineQubit.range(2)

#zpowergate with power of 0.25 because exponent=0.5 and need to do 1/2 of that according to https://github.com/quantumlib/Cirq/blob/a22269dfe41b0da78243bbd210a915d26cc7d25f/cirq-core/cirq/ops/swap_gates.py#L166 line 218
zPowGate = cirq.ops.ZPowGate(exponent=0.25)
negativeZPowGate = cirq.ops.ZPowGate(exponent=-0.25)

#cnot
cnot = cirq.ops.CNOT

#hadamard
h = cirq.ops.H


# Create rotation gates
theta = np.pi/4

# -theta
rz_minus_theta = cirq.Rz(rads=-theta)
# -theta + pi
rz_plus_pi = cirq.Rz(rads=-theta + np.pi)
# pi
rz_pi = cirq.Rz(rads=np.pi)
XGate = cirq.ops.X


# Create circuit and append everything together
circuit = cirq.Circuit()

# starting with a |1> state on 1 qubit 
circuit.append(XGate(q1))
#sqrt_iswap decompose @ line 212 https://github.com/quantumlib/Cirq/blob/a22269dfe41b0da78243bbd210a915d26cc7d25f/cirq-core/cirq/ops/swap_gates.py#L166
circuit.append(cnot(q0,q1))
circuit.append(h(q0))
circuit.append(cnot(q1,q0))
circuit.append(zPowGate(q0))
circuit.append(cnot(q1,q0))
circuit.append(negativeZPowGate(q0))
circuit.append(h(q0))
circuit.append(cnot(q0,q1))

circuit.append(rz_minus_theta(q0))
circuit.append(rz_plus_pi(q1))

#sqrt_iswap decompose @ line 212 https://github.com/quantumlib/Cirq/blob/a22269dfe41b0da78243bbd210a915d26cc7d25f/cirq-core/cirq/ops/swap_gates.py#L166
circuit.append(cnot(q0,q1))
circuit.append(h(q0))
circuit.append(cnot(q1,q0))
circuit.append(zPowGate(q0))
circuit.append(cnot(q1,q0))
circuit.append(negativeZPowGate(q0))
circuit.append(h(q0))
circuit.append(cnot(q0,q1))

circuit.append(rz_pi(q1))
circuit.append(cirq.measure(q0, q1, key='b')) # Measure both qubits


print(circuit)

result = service.run(program=circuit, repetitions=100)
print("Result from compilation:", result)
cost = service.estimate_cost(circuit, repetitions=100, target="ionq.qpu")
print("Estimated cost:")
print(cost.estimated_total)