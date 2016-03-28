month_days= [('January',[31]),('February',[28,29]),('March',[31]), ('April',[30]),('May',[31]),('June',[30]),('July',[31]),('August',[31]), ('September',[30]),('October',[31]),('November',[30]),('December',[31]) ]

day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


#1

def days_in_month(month):
  i=0
  for i in month_days:
    if month ==i[0]:return i[1]
  else: return 'error'


  #2

def day_of_week(day,month,year):
  zellar=     (((13*month+3) // 5+day+year+(year//4) - (year//100) + (year//400))%7)
  if month == 1 or month == 2:
    zellar2=  (((13*(month+12)+3) // 5+day+(year-1)+((year-1)//4) - ((year-1)//100) + ((year-1)//400))%7)
    return day_names[zellar2]
  else: return day_names[zellar]


  #3


  '''day = 13 and day of week =friday'''
def unlucky(year):
        days=[x for x in range(1,32) if x==13]
        months=[m for m in range(1,13)]
        can=[(x,y,year) for x in days for y in months]
        return [x for x in can if day_of_week(x[0],x[1],x[2])== 'Friday']

#4

def mostUnlucky(year):
        return [x for x in range(2016) if len(unlucky(x)) >=3]
                
def mostUnlucky2(year):
        a=[]
        for x in range(2016):
                if len(unlucky(x)) >=3:
                        a=a+[x]
        return a
