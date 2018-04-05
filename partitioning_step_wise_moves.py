f = open('creating_data_9.txt','r')
lines = f.readlines()
f.close()

temp = []

for line in lines:
	temp = line.strip().split(',')

	n = temp.count('-1')
	st = 'step_'+str(9-n)+'.txt'
	f = open(st,'a')
	f.write(line)
	f.close()
