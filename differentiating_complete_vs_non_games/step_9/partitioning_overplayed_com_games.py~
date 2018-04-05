n = 3
f = open('step_'+str(n)+'.txt','r')
lines = f.readlines()
f.close()

ref = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
temp = []


f1 = open('step_'+str(n)+'_non_complete_games.txt','w')
f2 = open('step_'+str(n)+'_complete_games.txt','w')
f3 = open('step_'+str(n)+'_over_played_games.txt','w')
f4 = open('step_'+str(n)+'_doubtly_over_played_games.txt','w')
for line in lines:
	count_1 = 0
	count_0 = 0
	temp = line.strip().split(',')
	for ref_line in ref:
		a = temp[ref_line[0]]
		b = temp[ref_line[1]]
		c = temp[ref_line[2]]
		if a==b and b==c :
			if a == '1':
				count_1 = count_1 + 1
			elif a == '0':
				count_0 = count_0 + 1
	if count_1 == 0:
		if count_0 == 0:
			f1.write(line)#non completed games
		elif count_0 == 1 : 
			f2.write(line)#completed games
		elif count_0 == 2:
			f4.write(line)#doubtly over played
		else:
			f3.write(line)#over played games
	elif count_1 == 1:
		if count_0 == 0:
			f2.write(line)#completed games
		else:
			f3.write(line)#over played games
	elif count_1 == 2:
		if count_0 == 0:
			f4.write(line)#doubtly over played
		else:
			f3.write(line)#over played games
	else:
			f3.write(line)#over played games	
f1.close()
f2.close()
f3.close()
f4.close()
