import os
import re
ls=os.listdir(os.getcwd())
print(ls)
for l in ls:
	pp = re.search("jpg",l) 
	if pp == None:
		pass
	else:
		os.remove(l)

