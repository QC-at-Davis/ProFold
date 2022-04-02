## Note on Requirements
* To submit jobs to the IonQ QPU via Azure Quantum, the python package `azure-quantum` needs to be installed. Currently `azure-quantum` seems to only be compatible with Cirq version 0.13.1 so you will need to explicitly declare the version number on installation of Cirq `pip install "cirq==0.13.1"`.

## Cirq/Pennylane Givens Definition differences
* Cirq definese the matrix for the Givens Rotation **WITHOUT** dividing the angle by two whereas Pennylane does this by default (all arguments to sine/cosine are theta/2).

## Relevant Files

* `IonQ-Givens-Cost-Estimation.ipynb` 
  * Defines an IonQ compatible Givens rotation gate, as well as an example of estimating the cost to run on the IonQ QPU
* `IonQ-Givens-Cirq-Simulation.ipynb`
  * Perform some tests to on the IonQ compatible Givens rotation to make sure it works as intended.
* `cirq-numpy-verification.ipynb`
  * Check the Google Cirq implementation of Givens against the Pennylane implementation. This notebook helped identify the fact that Cirq does not divide the provided angle by 2, a problem that caused discrepancies during verification.