"""sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "rubber baby buggy bumpers"
mS = "Experience is simply the name we given our mistake"
bS = "Tell me and I forgot and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,112,65,8,98]
eL = []
spL = ['name','adress','phone number','social security number']"""



sI = 45

if type(sI) == int:
	if sI <= 100:

		print'Thats a small number'


mI = 100

if type(mI) == int:
	if mI >=100:
		print'Big number'


eI = 0 
if type(eI) == int:
	if eI <= 0:
		print'Small'	

sS = "Rubber baby buggy bumpers"

if type(sS) == str:

	if sS.count > 50:
		print'short sentence'



bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."

if type(bS) == str:
	if bS.count > 50:
		print'long sentence'


mL = [3,5,7,34,3,2,113,65,8,89]
if type(mL) == list:
	if mL > 10:
		print'long list!!'


lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]

if type(lL) == list:
	if lL > 10:
		print'Very LONG list!'







