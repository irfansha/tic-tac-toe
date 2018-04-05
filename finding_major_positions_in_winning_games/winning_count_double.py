

f1 = open('observations.txt','a')

count_values = [0,0,0,0,0,0,0,0,0]
for i in range(5,10):
	f = open('double_step_'+str(i)+'_completed.txt','r')
	lines = f.readlines()
	f.close()
	for line in lines:
		temp = line.strip().split(',')
		for i in range(0,9):
			if line[i] == '1':
				count_values[i] = count_values[i]+1
f1.write('this is for winning total double positions in all steps'+str(count_values)+'\n')
f1.close()
