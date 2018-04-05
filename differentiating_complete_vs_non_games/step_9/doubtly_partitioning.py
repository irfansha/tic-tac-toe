n = 9
f = open('step_'+str(n)+'_doubtly_over_played_games.txt','r')
lines = f.readlines()
f.close()

ref = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
temp = []
check_list = [0,2,4,6,8]
f1 = open('astep_'+str(n)+'_doubt_games_completed.txt','w')
f2 = open('astep_'+str(n)+'_doubt_games_over_played.txt','w')
for line in lines:
	count_values = [0,0,0,0,0,0,0,0,0]
	temp = line.strip().split(',')
	for ref_line in ref:
		a = temp[ref_line[0]]
		b = temp[ref_line[1]]
		c = temp[ref_line[2]]
		if a==b and b==c and a != '-1':
				count_values[ref_line[0]] = count_values[ref_line[0]]+1
				count_values[ref_line[1]] = count_values[ref_line[1]]+1
				count_values[ref_line[2]] = count_values[ref_line[2]]+1
	flag = 0
	for i in range(len(count_values)):
		if count_values[i] == 2 and i in check_list:
			f1.write(line)#completed games
			flag = 1
			break
	if flag == 0:
		f2.write(line)#over played games
	
f1.close()
f2.close()

