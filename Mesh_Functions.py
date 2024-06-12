import math

def R_Newtons(s,L,n):
	TOL = 0.001
	R = 1 # Initial Guess
	Rprev = 0
	while abs(Rprev - R) > TOL:
		# Newton's Method
		f = 0
		fprime = 0
		for i in range (n):
			f = f + s*R**(i+1) 
			fprime = fprime + (i+1)*s*R**i
		f = f - L
		Rprev = R	
		R = R - f/fprime
	return R

def linear_mesh(s1, s2, L, n):
	R_f = R_Newtons(s1,L,n)
	R_b = R_Newtons(s2,L,n)

	mesh_f = []
	mesh_b = []
	L_f = s1*R_f
	L_b = s2*R_b
	for i in range(n):
		mesh_f.append(L_f)
		mesh_b.append(L_b) #Reverse order, i.e. mesh_b[0] refers to the same mesh element as mesh_f[n-1]
		L_b = L_b*R_b
		L_f = L_f*R_f

	mesh_final = []
	for i in range(n):
		mesh_final.append((mesh_f[i] + mesh_b[n-1-i])/2)	

	# Calculate MAX(|R-1|)
	ERR_final = []
	ERR_final.append(abs(1 - mesh_final[0]/s1))
	for i in range(n-1):
		ERR_final.append(abs(1 - mesh_final[i+1]/mesh_final[i]))
	ERR_final.append(abs(1 - s2/mesh_final[n-1]))
	
	ERR_final_b = []
	mesh_final_b = mesh_final[::-1]
	ERR_final_b.append(abs(1 - mesh_final_b[0]/s2))
	for i in range(n-1):
		ERR_final_b.append(abs(1 - mesh_final_b[i+1]/mesh_final_b[i]))
	ERR_final_b.append(abs(1 - s1/mesh_final_b[n-1]))
	
	return mesh_final, max(max(ERR_final), max(ERR_final_b))

def mesh_main(s1,s2,L):
	if L <= 0:
		raise SystemExit('Error: L domain must have positive width')
	if s1 <=0 or s2 <=0:
		raise SystemExit('Error: Boundary elements must have positive width')

	# Estimate number of elements
	n = round(L/((s1+s2)/2))
	if n == 0:
		n = 1

	Mesh, Err = linear_mesh(s1,s2,L,n)

	Search_D = 0
	if n == 1: # if n can only increase
		MeshINC, ErrINC = linear_mesh(s1,s2,L,n+1)
		if ErrINC < Err:
			Search_D = 1
			Mesh = MeshINC
			Err = ErrINC

	else:
		MeshINC, ErrINC = linear_mesh(s1,s2,L,n+1)
		MeshDEC, ErrDEC = linear_mesh(s1,s2,L,n-1)
		if ErrINC < ErrDEC and ErrINC < Err:
			Search_D = 1
			Mesh = MeshINC
			Err = ErrINC
		if ErrDEC < ErrINC and ErrDEC < Err:
			Search_D = -1
			Mesh = MeshDEC
			Err = ErrDEC

	if Search_D == 0:
		return Mesh, Err
	else:
		i = 2
		while 1:
			Mesh_Next, Err_Next = linear_mesh(s1, s2, L, n+(i*Search_D))
			if Err_Next > Err:
				break
			else:
				i+=1
				Mesh = Mesh_Next
				Err = Err_Next

				if i > 99:
					raise SystemExit('Error: Element number not converging')
	
	if max(Mesh) > s1 and max(Mesh) > s2:
		print("WARNING: Lmax > Smax\n s1 = " + str(s1) + ", s2 = " + str(s2) + ", L = " + str(L)) 	
	return Mesh, Err


