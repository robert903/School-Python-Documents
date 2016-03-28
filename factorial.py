'''factorials in iteration -for loop, while loop- and recursion augmenting and tail'''

def a_fac(intg):
	if intg==1:
		return 1
	else:
		return intg*a_fac(intg-1)
	
 	
	
	
	
	
	
	
def t_fac(intg):
	def f(i,res):
		if i>intg:
			return res
		else:
			return f(i+1,res*i)
	return f(1,1)
	
	
	
	


def f_fac(intg):
	f=1
	for i in range(1,intg+1):
		f=f*i
	return f
	
	
	
	
def w_fac(intg):
	f=1
	while intg>1:
		f=f*intg
		intg=intg-1
	return f