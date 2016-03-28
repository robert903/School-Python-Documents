def _zip(list1,list2):
	return zip(list1,list2)
	
	
'''def ziprec(list1,list2):
	return [(x,y) for x in list1 and y in list2:'''
	
def zip2(list1,list2):
	if list1==[]:
		return []
	else:
		return [(list1[0],list2[0])] + zip2(list1[1:],list2[1:])
		
		
def double(list,f):
	if list==[]:
		return []
	else: return [f(list[0])] + double(list[1:],f)
	
def _map(f,list):
	return [f(x) for x in list]
	
def _map2(f,list):
	newlist=[]
	while list!=[]:
		newlist+=[f(list[0])]
		list=list[1:]
	return newlist