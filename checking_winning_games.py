f = open('creating_data_9.txt','r')
lines = f.readlines()
f.close()

ref = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
temp = []

for line in lines:
	temp = line.strip().split(',')
	for ref_line in ref:
		a = temp[ref_line[0]]
		b = temp[ref_line[1]]
		c = temp[ref_line[2]]
		if a==b and b==c and a != '-1':
			print ('true')
		else:
			print('flase')
	print('##########')
	

