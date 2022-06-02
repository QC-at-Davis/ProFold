# ProFold
A molecular dynamics approach to protein folding, using GROMACS with CHARMM on an FPGA for classical molecular modeling and the Variational Quantum Eigensolver (VQE)/Quantum Fourier Transform (QFT) for modeling the electronic shells of each atom. 

# Why? 
Molecular dynamics methods are the gold standard for protein folding, as it allows for easy setup of a solvent and other environmental details that can effect the folding. However, at the least, 1 microsecond of protein movement needs to be completed to gain an accurate fold, as detailed here (https://www.bu.edu/caadlab/Khan13.pdf). Considering that GPUs can only achieve around 100 ns/day of modeling (https://arxiv.org/abs/2201.06372), it would take at least 10 days on one of these devices to get to a basic folded structure using GROMACS with CHARMM.

However, this scaling gets worse when also including the electronic bases of each atom in quantum based modeling. While CHARMM scales in O(N^2) (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810661/), quantum based methods scale in O(N^4) (https://pubs.rsc.org/en/content/articlelanding/2022/sc/d1sc05691c?ref=banner). 

For these reasons, this project aims to combined the best in classical modeling - FPGA based CHARMM models, such as this one (https://www.bu.edu/caadlab/hprcta_09.pdf) - with quantum methods - VQE and/or QFT for electronic shell modeling, such as this one (https://pubs.rsc.org/en/content/articlelanding/2022/sc/d1sc05691c?ref=banner)  - in order to create a faster, more accurate pipeline for protein folding. We aim to submit these results to CASP15 (https://www.predictioncenter.org/casp15/).



# What is this project? How do I interact with it? 
This project is a collaborative, open source piece of work. There is no stable verison that can be picked up and used as of yet. Certain features can be run as scripts on their own, but full integration is still to be completed.

If you would like to add to the project, take a look at the Issues, fork the repo, start working away at them, and submit PRs. Feel free to also come to QCAD meetings, join the Discord(https://discord.gg/8VCtsuve), or add an issue for the project if you would like to chat about other additions to the project or current problems. 


# High Level Overview of How This Would Work

1. Translate FASTA sequences of amino acids into 3D monomer files by using Open Babel 2.4.1 (https://sourceforge.net/projects/openbabel/files/openbabel/2.4.1/) (NOTE: Only this version accurately translates over the amino acid columns to the PDB, the newest version does not) 

2. Run this monomer within a water model in GROMACS with CHARMM, following these steps (https://manual.gromacs.org/current/user-guide/flow.html), saving energy values and PDB

3. Take PDB ouputted from step 2, find Gaussian bases, and make a quantum circuit with those bases 

4. Complete VQE or QFT on these bases to find ground state energy 

5. Inverse fourier transform the results to regain coordinates for an updated PDB

6. Compare results to other protein structures using Topological Data Analysis (TDA) tools such as Ripser++ (https://github.com/simonzhang00/ripser-plusplus)


# Getting Started
Packages Needed:
1. anaconda3 https://docs.anaconda.com/anaconda/install/linux/
2. qsharp and all its related tooling https://docs.microsoft.com/en-us/azure/quantum/install-python-qdk?tabs=tabid-conda
3. pennylane: https://pypi.org/project/PennyLane/  
4. pennylane-qsharp: https://github.com/PennyLaneAI/PennyLane-qsharp
5. tensorflow (if you want to use the tensorflow pennylane interface to get some speedup https://pennylane.readthedocs.io/en/stable/introduction/interfaces/tf.html#tf-interf) https://www.tensorflow.org/install/pip
 
