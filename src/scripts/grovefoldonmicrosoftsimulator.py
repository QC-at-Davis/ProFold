import pennylane as qml
from numpy import random 
import math
import numpy as np
def groversAlgorithm(subgraphRotations=None, oracalizedRotation=None, simulationEnvironment="microsoft.QuantumSimulator",providedInterface=None,numWires=20):
    #max number of wires that can be taken = 30, but lets scale it based on the number of cores accessible 
    #Time taken in seconds on QDK: 310.7244839668274 for 20 qubits on i7 laptop, 26 qubits did not show results even after >1 hr
    #Time taken in seconds on Pennylane with tensorflow with 25 qubits =  1049.3635635375977s on intel i7 laptop in CPU mode 
    #Time taken in seconds on Pennylane with tensorflow with 20 qubits = 4.4838268756866455 s 
    shotAmt = int(math.sqrt(2**numWires))
    dev = qml.device(simulationEnvironment, wires=numWires, shots=shotAmt)
    #first, we need to create the rotations on the qubits so as to represent the different subgraphs 
    @qml.qnode(dev,interface=providedInterface)
    def groverCircuit(simulationEnvironment, subgraphRotations,oracle,wires):
        if subgraphRotations == None:
            subgraphRotations = [random.rand() for i in range(0,wires)]
            for i in range(0,wires):
                qml.Rot(subgraphRotations[i],subgraphRotations[i],subgraphRotations[i] ,wires=i)
                #qml.RX(subgraphRotations[i] ,wires=i)
            print("Using Random Rotations from Numpy",subgraphRotations)
        else:
            for i in range(0,wires):
                qml.RZ(subgraphRotations[i] ,wires=i)
                #qml.RX(subgraphRotations[i] ,wires=i)
        if oracle == None:
            oracle = subgraphRotations[19]
        print("Oracle", oracle)
        for i in range (0,wires):
            qml.Hadamard(i)
        for i in range (0,wires-1):
            qml.RZ(oracle, wires=i)

        qml.MultiRZ(oracle,wires=[i for i in range(0,wires)])
        qml.Hadamard(i)
        for i in range (0,wires):
            qml.PauliX(wires=i)
        
        #multiRZ not working on microsoft, only with default.qubit
        qml.MultiRZ(math.pi/4,wires=[i for i in range(0,wires)])
        for i in range (0,wires):
            qml.PauliX(wires=i)
        for i in range (0,wires-1):
            qml.Hadamard(i)
        # qml.probs(wires=[0,1]) gets a MeasurementProcess eror from pennylane_qsharp :( so sadly have to use use one of the observable functions https://pennylane.readthedocs.io/en/stable/introduction/measurements.html
        if(simulationEnvironment == "default.qubit"):
            probs = qml.probs(wires=[i for i in range(0,wires)])
            return probs 
        else:
            measurementResults = [qml.expval(qml.Hadamard(wires=(i))) for i in range(0,wires)]
            return measurementResults
    output = groverCircuit(simulationEnvironment, subgraphRotations,oracalizedRotation,numWires)
    maxProb = np.amax(output.numpy())
    maxIndex = np.where(output.numpy() == maxProb)
    return [maxIndex, maxProb]
# if __name__ == '__main__':
