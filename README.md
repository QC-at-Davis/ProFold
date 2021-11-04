# GroveFold
Attempt at protein folding utilizing Grover's Search Algorithm 

# Why? 
One of the fastest search algorithms for large datastores was one designed by Lov Grover at Bell Labs in the late 1990s, which focuses on taking states from quantum bits, or qubits, and inversing the amplitude of the wavelength on each qubit by the mean amplitude of all qubits after the application of the rotation of the qubit, known as an oracle step, one is looking for to see what which qubit is to that output rotation (https://dl.acm.org/doi/pdf/10.1145/237814.237866?casa_token=Fzv_S6TcwzEAAAAA%3Ah0xNTFldKN6XAljMZt9Slzg_ma-Q0w6cfx7PgF0OzmUT8fglYpNGHEUm2t71-35cGAFiglHvOlk). In completing this process on a superconducting qubit, one inadvertently is determining the most electronically excited of the qubits in some formation given the rotation provided, as this "Grover's Effect" has been seen in actual electronic stuctures (https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.180501). For this reason, we theorize that Grover's Search Algorihtm could be utilized for determing the folding pattern of proteins by utilizing qubits as analogues for the electronic states of the atoms and the oracle state resulting from electronic interactions with water or the solvent a protein is in.

# What is this project? How do I interact with it? 
This project is an truly collaborative, open source piece of work. There is no stable verison that can be picked up and used as of yet. 

To use the latest version of the project, make sure to clone this git repo, install the right packages, and run from the "main.py" script. 

If you would like to add to the project, take a look at the Issues, fork the repo, start working away at them, and submit PRs. Feel free to also come to QCAD meetings,join the Discord(https://discord.gg/8VCtsuve), or add an issue for the project if you would like to chat about other additions to the project or current problems. 


# High level road map

1. Allow for breakup of PDB files into subgraphs with electronic details that water based oracles can be applied to for a base folding system using Pennylane from Xanadu with the Tensorflow interface to allow for easy testability and scalability classically (https://pennylane.ai/qml/demos/qsim_beyond_classical.html) 
2. Run some tests that determine the effectiveness of this algorithm (Feel free to suggest some cases in the issues)
3. Testing and comparison with physical quantum device, such as the IonQ device https://docs.microsoft.com/en-us/azure/quantum/tutorial-qdk-grovers-search?tabs=tabid-visualstudio 


# Getting Started
Packages Needed:
1. anaconda3 https://docs.anaconda.com/anaconda/install/linux/
2. qsharp and all its related tooling https://docs.microsoft.com/en-us/azure/quantum/install-python-qdk?tabs=tabid-conda
3. pennylane: https://pypi.org/project/PennyLane/  
4. pennylane-qsharp: https://github.com/PennyLaneAI/PennyLane-qsharp
5. tensorflow (if you want to use the tensorflow pennylane interface to get some speedup https://pennylane.readthedocs.io/en/stable/introduction/interfaces/tf.html#tf-interf) https://www.tensorflow.org/install/pip
 
