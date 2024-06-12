# 1D-Mesh
Function to mesh a 1D interval with smoothly changing element sizes

This includes 2 code files: Mesh_Functions.py and Mesh_Tests.py

Mesh_Functions.py contains the function "Mesh,Err = mesh_main(s1,s2,L)"
This function takes in element sizes s1 and s2 at the end of the 1D-interval of width L and produces a mesh with maximal 'smoothness'. (Element sizes change gradually across the width of the mesh).
'Mesh' is a list of element sizes spanning from s1 to s2, non-inclusive of s1 and s2. (len(Mesh) is the number of elements).
'Err' is a smoothness measure for 'Mesh'. (Minimal Err -> Maximum Smoothness).

Mesh_Tests.py contains a plotting function "Mesh_Plot(s1,s2,L,mesh)", which plots the s1 element as a red line, the s2 element as a blue line, and the intermediate mesh nodes as black tick marks. Running the file Mesh_Tests.py will display plots for a short series of test cases.

The mathematical foundation for this algorithm is described in 1D_Meshing.pdf
