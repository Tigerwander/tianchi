import csv
user_record_file='tianchi_mobile_recommend_train_user.csv'
read_handle=open(user_record_file,'r')
user_dict={}
for line in read_handle:
	user_ope=line.strip('\n').split(',')
	user=user_ope[0]
	goods=user_ope[1]
	operation=user_ope[2]
	category=user_ope[4]
	time=user_ope[5]
	if user in user_dict:
		if time in user_dict[user]:
			if category in user_dict[user][time]:
				if goods in user_dict[user][time][category]:
					user_dict[user][time][category][goods].append(operation)
				else:
					operation_list=[]
					operation_list.append(operation)
					user_dict[user][time][category][goods]=operation_list
			else:
				operation_list=[]
				operation_list.append(operation)
				goods_dict={}
				goods_dict[goods]=operation_list
				user_dict[user][time][category]=goods_dict
		else:
			operation_list=[]
			operation_list.append(operation)
			goods_dict={}
			goods_dict[goods]=operation_list
			category_dict={}
			category_dict[category]=goods_dict
			user_dict[user][time]=category_dict
	else:
		operation_list=[]
		operation_list.append(operation)
		goods_dict={}
		goods_dict[goods]=operation_list
		category_dict={}
		category_dict[category]=goods_dict
		time_dict={}
		time_dict[time]=category_dict
		user_dict[user]=time_dict

'''
# sort the item record by time
for user in user_dict:
	for category in user_dict[user]:
		for item in user_dict[user][category]:
			user_dict[user][category][item].sort(key=lambda x:x[1])
'''
# save purchase behavior

purchase={}
for user in user_dict:
	for time in user_dict[user]:
		for category in user_dict[user][time]:
			for goods in user_dict[user][time][category]:
				if user_dict[user][time][category][goods].count('4'):
					if user in purchase:
						if time in purchase[user]:
							purchase[user][time].append(user_dict[user][time][category][goods])
						else:
							purchase[user][time]=[]
							purchase[user][time].append(user_dict[user][time][category][goods])
					else:
						time_dict={}
						time_dict[time]=[]
						time_dict[time].append(user_dict[user][time][category][goods])
						purchase[user]={}
						purchase[user]=time_dict


write_file='purchase_record.txt'
write_handle=open(write_file,'w')
'''
for user in user_dict:
	write_handle.write('%s:\n'%user)
	for time in user_dict[user]:
		write_handle.write('	%s:\n'%time)
		for category in user_dict[user][time]:
			write_handle.write('		%s:\n'%category)
			for goods in user_dict[user][time][category]:
				write_handle.write('			%s:'%goods)
				for operation in user_dict[user][time][category][goods]:
					write_handle.write('%s '%operation)
				write_handle.write('\n')
'''

for user in purchase:
	write_handle.write('%s\n'%user)
	for time in purchase[user]:
		write_handle.write('	%s\n:'%time)
		for record in purchase[user][time]:
			write_handle.write('		')	
			for item in record:
				write_handle.write('%s '%item)
			write_handle.write('\n')
write_handle.close()


