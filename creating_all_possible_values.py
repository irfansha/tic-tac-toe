#+o)
fin = 9
num = 1
l = [-1,0,1]


for i in range(1,fin):
	f = open('creating_data_'+str(i)+'.txt','r')

	lines = f.readlines()

	f.close()

	f1 = open('creating_data_'+str(i+1)+'.txt','w')
	for n in l:
		for line in lines:
			f1.write(str(n)+','+str(line))
	f1.close()
	




