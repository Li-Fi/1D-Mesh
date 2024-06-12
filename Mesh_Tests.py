from Mesh_Functions import *
import matplotlib.pyplot as plt
import numpy as np

def Mesh_Plot(s1,s2,L,mesh):
	s1_points = [0, 0+s1]
	s2_points = [s1+L, s1+L+s2]
	fig, ax = plt.subplots()
	ax.plot(s1_points, [0,0], 'r|-')
	ax.plot(s2_points, [0,0], 'b|-')

	mesh_nodes = []
	for i in range(len(mesh)-1):
		if i == 0:
			mesh_nodes.append(mesh[i] + s1)
		else:
			mesh_nodes.append(mesh[i] + mesh_nodes[i-1])

	ax.plot(mesh_nodes, [0]*len(mesh_nodes), 'k|')	
	return fig, ax

##############
# MESH TESTS #
##############

Test_Data = np.array([
						[1,1,10],#1
						[1,5,10],#2
						[5,1,10],#3
						[5,5,1], #4
						[1,2,100],#5
					])

Test_Titles = [
				"Test 1: Exact case, Rmax = 0",
				"Test 2: Typical case, s1 < s2",
				"Test 3: Typical case, s1 > s2",
				"Test 4: L <<< s",
				"Test 5: Large L",
				]

n = Test_Data.shape
for i in range (n[0]):

	s1 = Test_Data[i,0]
	s2 = Test_Data[i,1]
	L = Test_Data[i,2]
	Mesh, Err = mesh_main(s1,s2,L)

	fig, ax = Mesh_Plot(s1,s2,L,Mesh)
	ax.set(title=Test_Titles[i])
	caption1 = "s1 = " + str(s1) + ", s2 = " + str(s2) + ", L = " + str(L)
	caption2 = "n = " + str(len(Mesh))
	caption3 = "Lmax = " + '%.5f'%max(Mesh) + ", Lmin = " + '%.5f'%min(Mesh) + ", Ltotal = " + '%.5f'%sum(Mesh)
	caption4 = "Rmax = " + '%.3f'%Err
	ax.text(0.95, 0.15, caption1 + "\n" + caption2 + "\n" + caption3 + "\n" + caption4, 
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=10)

	plt.show()
	#fig.savefig("test.png")

	


