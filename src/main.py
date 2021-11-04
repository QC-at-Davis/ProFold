from scripts.grovefoldonmicrosoftsimulator import groversAlgorithm

import time 

if __name__ == '__main__':
	t0 = time.time()
	for i in range(0,100000):
		output = groversAlgorithm(simulationEnvironment="default.qubit", providedInterface="tf",numWires=20)
		print(output)
	t1 = time.time()
	print("Time taken in seconds:", (t1-t0))

