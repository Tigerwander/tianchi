import csv

def found_purchase(time_dict):
	for time in time_dict:
		if time_dict[time].count('4')!=0:
			return True
	return False

def sort_dict(time_dict):
	time_list=[(time,time_dict[time]) for time in sorted(time_dict.keys())]
	return time_list


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
		if goods in user_dict[user]:
			if time in user_dict[user][goods]:
					user_dict[user][goods][time].append(operation)
			else:
				user_dict[user][goods][time]=[]
				user_dict[user][goods][time].append(operation)
		else:
			time_dict={}
			time_dict[time]=[]
			time_dict[time].append(operation)
			user_dict[user][goods]=time_dict
	else:
		time_dict={}
		time_dict[time]=[]
		time_dict[time].append(operation)
		goods_dict={}
		goods_dict[time]=time_dict
		user_dict[user]=goods_dict

#collect purchase behavior
'''
purchase_dict={}
for user in user_dict:
	for goods in user_dict[user]:
		if found_purchase(user_dict[user][goods]):
			if user in purchase_dict:
				purchase_dict[user][goods]=user_dict[user][goods]
			else:
				goods_dict={}
				goods_dict[goods]=user_dict[user][goods]
				purchase_dict[user]=goods_dict
'''

purchase_dict=user_dict
#sort the purchasing date
for user in purchase_dict:
	for goods in purchase_dict[user]:
		purchase_dict[user][goods]=sort_dict(purchase_dict[user][goods])

# save user purchase behavior
write_file='full_record.txt'
write_handle=open(write_file,'w')
for user in purchase_dict:
	write_handle.write('%s:\n'%user)
	for goods in purchase_dict[user]:
		write_handle.write('	%s:\n'%goods)
		for time_tuple in purchase_dict[user][goods]:
			write_handle.write('		%s:'%time_tuple[0])	
			time_tuple[1].sort()
			for operation in time_tuple[1]:
				write_handle.write('%s '%operation)
			write_handle.write('\n')
write_handle.close()


