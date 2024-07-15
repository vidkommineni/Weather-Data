file = "WeatherDataCLL.csv"
with open (file,"r") as file:
     datas = file.read().split('\n')

#created a list of variables that I need to store values for
count=1
wSpd=[]
prcp=[]
aTemp=[]
maxTemp=[]
minTemp=[]
date=[]

#created a dictionary for months, for the second half of the code. Months associated with nums
monthDict = {'January':1,
             'February':2,
             'March':3,
             'April':4,
             'May':5,
             'June':6,
             'July':7,
             'August':8,
             'September':9,
             'October':10,
             'November':11,
             'December':12}

#keep looping
while True:
    #chekcing to make sure it is not out of bounds
    if count >=len(datas)-1:
        break
    #splitting each line into a list
    line=datas[count]
    lineList=line.split(',')
    #taking the index of the values in the list, and appending them into correct value lists. 
    date.append(lineList[0])
    wSpd.append(float(lineList[1]))
    prcp.append(float(lineList[2]))
    aTemp.append(int(lineList[3]))
    maxTemp.append(int(lineList[4]))
    minTemp.append(int(lineList[5]))
    #the count increases by one
    count+=1
    
    #getting the abs max and min and calculating the avg percipitation
absMaxTemp = max(maxTemp)
absMinTemp = min(minTemp)
avgPrcp = sum(prcp)/len(prcp)


#printing the calculated calues
print(f'3-year maximum temperature: {absMaxTemp} F')
print(f'3-year minimum temperature: {absMinTemp} F')
print(f'3-year average precipitation: {avgPrcp:.3f} inches')

print()

#getting a month and year from the user
uMonth = input('Please enter a month: ')
uYear = input('Please enter a year: ')
print()


#creating variable lists that will be used later
month = monthDict[uMonth]
monthMax = []
monthWind = []
monthRain = []

acc = 0
#checking the vals in date list
for index in date:
    #checking to see if the first 2 vals are nums
    if index[0:2].isnumeric():
        if uYear in index:
            if index[0:2] == str(month):
            #if the condition is met, then the value is added to max. 
                monthMax.append(int(maxTemp[date.index(index)]))
            #adding the max wind from the specified date
                monthWind.append(float(wSpd[date.index(index)]))
            #adding the rain from the given day
                monthRain.append(prcp[date.index(index)])
    else:
        if uYear in index:
            if index[0:1] == str(month):
                monthMax.append(int(maxTemp[date.index(index)]))
                monthWind.append(float(wSpd[date.index(index)]))
                monthRain.append(prcp[date.index(index)])
for rain in monthRain:
    if rain!=0.0:
        acc+=1
if len(monthRain)!=0:per=round((acc/len(monthRain))*100,1)
else: per=0.0
if len(monthMax)!=0:mean=round(sum(monthMax)/len(monthMax),1)
else: mean=0
if len(monthWind)!=0:mean1=sum(monthWind)/len(monthWind)
else:mean1=0
mean1='%.2f' % mean1



print(f'For {uMonth} {uYear}:')
print(f'Mean maximum daily temperature: {mean} F')
print(f'Mean daily wind speed: {mean1} mph')
print(f'Percentage of days with precipitation: {per}%')
#print(date)









