import csv
user_record_file='tianchi_mobile_recommend_train_user.csv'
read_handle=open(user_record_file,'r')
user_dict={}
for line in read_handle:
	user_ope=line.strip('\n').split(',')
	ope_record=[user_ope[1],user_ope[2],user_ope[5]]
	if user_ope[0] in user_dict:
		if user_ope[4] in user_dict[user_ope[0]]:
			user_dict[user_ope[0]][user_ope[4]].append(ope_record)
		else:
			user_dict[user_ope[0]][user_ope[4]]=[]
			user_dict[user_ope[0]][user_ope[4]].append(ope_record)
	else:
		user_dict[user_ope[0]]={}
		ope_dict={}
		ope_dict[user_ope[4]]=[]
		ope_dict[user_ope[4]].append(ope_record)
		user_dict[user_ope[0]]=ope_dict
read_handle.close()

write_file='user_operation_record.txt'
write_handle=open(write_file,'w')
for user in user_dict:
	write_handle.write('%s:\n'%user)
	for category in user_dict[user]:
		write_handle.write('	%s:\n'%category)
		for ope_record in user_dict[user][category]:
			write_handle.write('		')
			for item in ope_record:
				write_handle.write('%s '%item)
			write_handle.write('\n')

write_handle.close()


