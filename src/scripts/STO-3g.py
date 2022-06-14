import pennylane as qml
import numpy as np
import tensorflow as tf

wires = 3

dev = qml.device('default.qubit', wires=wires)

@qml.qnode(dev, interface='tf')
def circuit_qft(basis_state):
    qml.BasisState(basis_state, wires=range(wires))
    qml.QFT(wires=range(wires))
    return qml.state()

state = tf.Variable([1.0, 0.0, 0.0])
newstate = circuit_qft(np.array([1.0, 0.0, 0.0]))




