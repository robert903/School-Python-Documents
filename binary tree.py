tree= [2,3,4,'t','n']

def makeT(r,ltr,rtr):
	tree= [r,ltr,rtr]
	return tree
	
def isbT(tree):
	if len(tree)==3 and type(tree)==list : return True
	else: return False
	
def isET(tree):
	return tree==[]
	
def getroot(tree):
	return tree[0]
	
def getltr(tree):
	if isbT(tree): return tree[1]
	
def getrtr(tree):
	if isbT(tree): return tree[2]
	
def inTree1(tree):
	if type(tree[0])==int or type(tree[1])==int or type(tree[2])==int: return True
	else: return False
	
	
	
	
#might not work idk
def inTree(x,tree):
	def helper(t):
		if getroot(t)==x:
			return True
		elif isET(t):
			return False
		elif getroot(t)>x:
			return helper(getltr(t))
		else: return helper(getrtr(t))
	if isbT(tree):
		return helper(tree)
		
	elif isET(tree):
		return False
	else:
		return 'error'