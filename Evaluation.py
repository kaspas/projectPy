def Evaluation(Word1,Word2):
	if len(Word1)<len(Word2):
		mini=len(Word1)
		maxi=len(Word2)
	else:
		mini=len(Word2)
		maxi=len(Word1)

	SameValue=0 # counter to poso idia eiani ta 2 string 
	for i in range(0,mini):
		if Word1[i]==Word2[i]:
			SameValue=SameValue+1

	SameValue=float(SameValue)
	EvalPersent=(SameValue/maxi)*100
	

	return EvalPersent

Eval=Evaluation('miltos','miltiadis')

print Eval
