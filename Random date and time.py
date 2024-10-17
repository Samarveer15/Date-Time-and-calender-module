import random
import time

def getRandomDate(startdate , endDate):
    print("Printing random date between", startdate, "and",endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%y'


    startTime = time.mktime(time.strptime(startdate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * ( endtime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date =",getRandomDate("1/1/2016","12/12/2018"))