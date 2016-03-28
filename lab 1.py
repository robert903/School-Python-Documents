month_days= [('January',[31]),('February',[28,29]),('March',[31]), ('April',[30]),('May',[31]),('June',[30]),('July',[31]),('August',[31]), ('September',[30]),('October',[31]),('November',[30]),('December',[31]) ]

day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


#1

def days_in_month(month):
	i=0
	for i in month_days:
		if month ==i[0]:return i[1]
	else: return 'error'
	
	
'''day = (((13*m+3) // 5 + d + y + (y // 4) - (y // 100) + (y // 400)) %7)
where
d = day, y = year and m = month

Note if the month is January or February then you add 12 to the month and subtract 1 from the year before calculating the day.

e.g. day_names[0] = Monday and day_names[6] = Sunday.
Define a python function day_of_week, which displays the day name for a given date supplied in the form (day,month,year).
e.g.
   >>> day_of_week(13,10,2015)
   'Tuessday'
   >>> day_of_week(23,10,2015)
   'Friday'
   >>> day_of_week(26,2,2015)
   'Thursday' '''

#2

def day_of_week(day,month,year):
	zellar=     (((13*month+3) // 5+day+year+(year//4) - (year//100) + (year//400))%7)
	if month == 1 or month == 2: 
			zellar2=  (((13*(month+12)+3) // 5+day+(year-1)+((year-1)//4) - ((year-1)//100) + ((year-1)//400))%7)
			return day_names[zellar2]
	else: return day_names[zellar]
	
	
	#3
	''' Using list comprehension, define a python function unlucky, which returns all the days in a given year which have the date Friday 13th e.g.
         unlucky(2010)
        [(13, 8, 2010)]
         unlucky(2005)
        [(13, 2, 2015), (13, 8, 2015), (13, 11, 2015)] 
[Hint: you need two ranges one for day starting from 1 and going to 31 and another one for month starting from 1 going to 12. Using these and the year which comes as an argument and use the function day_of_week in the if part of list comprehension to check if a given date is Friday and also check if the day is equal to 13.] 
'''

'''def RAPlist(num):       #10
    final= [x for x in range(1,num+1) if revAndPrime(x)==True] 
    return final'''
    
#def unlucky(year):

''' if 13th of each month == friday represent in a list'''