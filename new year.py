import datetime
 

countdown = lambda : datetime.datetime(2019, 1, 1, 00, 00) - datetime.datetime.now()

print(countdown())


# import time
# import datetime
 
# m = input('month: ')
# d = input('day: ')
# now_date = datetime.date.today() # Текущая дата (без времени)
# now_time = datetime.datetime.now() # Текущая дата со временем
 
# cur_year = now_date.year # Год текущий
# cur_month = now_date.month # Месяц текущий
# cur_day = now_date.day # День текущий
 
# countdown = lambda : datetime.datetime(2015,1,1,00,00) - datetime.datetime.now()
 
# if m == cur_month and d == cur_day:
   
#     print countdown()
   
# else: print 'date error'