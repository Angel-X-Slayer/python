def TowerOfHanoi(n , source, destination, auxiliary):## A, C, B are the name of rods
													 ## A=source, B=destination, C=auxiliary
	if n==1:
		print ("Move disk 1 from",source,"to",destination,end="\n\n")
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from",source,"to",destination,end="\n\n")
	TowerOfHanoi(n-1, auxiliary, destination, source)
		

n = 3
TowerOfHanoi(n,'source','destination','auxilary')