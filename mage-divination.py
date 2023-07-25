data = []
while True:
	M = int(input('請輸入月份:'))
	if M > 12 or M < 1:
		print('輸入錯誤，請重新輸入')
	else:
		data.append(M)
		break
		
while True:
	D = int(input('請輸入日期:'))
	
	if (M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12):
		if D > 31 or D < 1:
			print(str(M)+'月的日期區間為1~31，請重新輸入!')
		else:
			data.append(D)
			break	
	elif (M == 2) :
		if D > 29 or D < 1:
			print(str(M)+'月的日期區間為1~29，請重新輸入!')
		else:
			data.append(D)
			break
	elif (M == 4 or M == 6 or M == 9 or M == 11) and (D > 30):
		if D > 30 or D < 1:
			print(str(M)+ '月的日期區間為1~30，請重新輸入!')
		else:
			data.append(D)
S = ((data[0] * 2 + data[1]) % 3)

if S == 0:
	print('凶')
elif S == 1:
	print('吉')
elif S == 2:
	print('大吉')
