#%%
# import math
# import os
print("Hello world!")

 


#%%
###############  HW  Week02      HW  Week02      HW  Week02    ###############
# Our Goal: print out the 366 days in 2020
# 2020/1/1 
# 2020/1/2 and so forth

from datetime import date, timedelta
First_date = date(2020, 1, 1)
Last_date = date(2020, 12, 31)
for i in range(((Last_date - First_date).days) + 1):
   print((First_date + timedelta(i)).strftime("%Y/%m/%d"))


#this variable stores the year which is 2020
year = 2020
#this variable stores the current month 1 represents January and so on
month = 1
#this variable represents the date
day = 0
#this is a list of weekdays
days = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
#since 2020/1/1 was a Wednesday so cnt = 3 to begin with
cnt = 3
#this is a list of all the months that have 30 days
Month30 = [4,6,9,11]
#this is a list of all the months that have 31 days
Month31 = [1,3,5,7,8,10,12]
#this is the month that contains the leap day
Month_leap = [2]
#the loop will run for 366 times i.e. for each day
for d in range(366):
#the loop is divided in three conditions, whether the current month is of 30, 31 or 29 days
#if the month is of 30 days it will be present in the Month30 list hence this block will take control
if month in Month30:
#date is set to 0
day = 0
#a loop is run for 30 times
for i in range(30):
#day is incremented by 1 each time
day += 1
#the day is printed along with the weekDay
print(year,"/",month,"/",day," ",days[cnt])
#The weekDay is incremented
cnt += 1
#if cnt is 7 that means at 6 it was 'Sat' and now needs to go back to 'Sun '
if cnt == 7:
#So cnt is is made to store 0
cnt = 0
#The month is incremented by 1
month += 1
#if the month has 31 days it will be present in the Month31 list
elif month in Month31:
day = 0
#This loop will now run for 31 times
for i in range(31):
day += 1
print(year,"/",month,"/",day," ",days[cnt])
#Similar logic as above for the weekdays
cnt += 1
if cnt == 7:
cnt = 0
#Month is incremented
month += 1
#If the month is 2 this block will take control
elif month in Month_leap:
day = 0
#Code runs for 29 times
for i in range(29):
day += 1
print(year,"/",month,"/",day," ",days[cnt])
#same logic as above for weekdays
cnt += 1
if cnt == 7:
cnt = 0
#month is incremented
month += 1


#%%
###################################### Q1 ###############################
#

dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
year = 2020
cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one
m = 0 # this will be a variable to be looped through eventually. I use the convention of 0-11 for the twelve months 
month = m+1 # this is the month to be displayed/printed. The way it is set up now, it will NOT change automatically when you change the value of m. Beware of that.
maxdays = 7 # this variable will be conditional on the month eventually. Right now, just try 7
# write a for loop, to print out the day value
# fill in the ??????

#If the month is 2 this block will take control
for i in range(31):
    day = i+1
print(year,"/",month,"/",day," ",dowt[cnt])

#%%
###################################### Q2 ###############################
#

# dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
year = 2020
# cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one
m = 3 # this will be a variable to be looped through eventually. I use the convention of 0-11 for the twelve months 
# month = m+1 # this is the month to be displayed/printed. The way it is set up now, it will NOT change automatically when you change the value of m. Beware of that.

# write a condition statement to determine the maxdays depending on the m value.
# For example, when m=0 (Jan), maxdays should be 31, m=3 (Apr), maxdays should be 30, etc.
# Try both ways, as a chunk of codes, or a one-liner
maxdays = ?????
print(maxdays)
#
# Change your m value (between 0 and 11, inclusive) and run the chunk to see if prints out the correct result.
#
# Challenge: if you can take into account that year is multiple of 4, EXCEPT when year is multiple of 100, the days 
# in Feb should be 29. Otherwise, there should be 28.  
# Examples: 2004, 2008, 2012, Feb has 29 days, but 2001, 2002, 2003, 2005, 2006, ... 28 days. Year 2000 or any 
# century marks, multiples of 100, they are non-leap years, so only 28 days.

#%%
###################################### Q3 ###############################
#

dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
# year = 2020
cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one
# m = 3 # this will be a variable to be looped through eventually. I use the convention of 0-11 for the twelve months 
#
# As the cnt value changes, we want to print out the day-of-week info.
# So 3 gives Wed, 7 gives Sat, 8 should gives Sun, and so forth.
# use the very common method of finding the remainder (mod 7), print out that info in a single line of code


#%%
###################################### Q4 ###############################
# Put all these together, and print out something like this: 
# Wed - 2020/1/1
# Thu - 2020/1/2
# Fri - 2020/1/3
# Sat - 2020/1/4
# Sun - 2020/1/5
# Mon - 2020/1/6
# Tue - 2020/1/7
# Wed - 2020/1/8
# Thu - 2020/1/9
# Fri - 2020/1/10
# Sat - 2020/1/11
# Sun - 2020/1/12
# Mon - 2020/1/13
# Tue - 2020/1/14
# Wed - 2020/1/15
# Thu - 2020/1/16

dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
year = 2020
cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one

for m in ????? : # loop thru the 12 months
  month = ???????
  maxdays = ????????
  for d in ???????:
    day = d+1
    dow = ??????????  # day of week 
    print("???????/????/????" % (dow,year,month,day) )
    cnt = ??????  # advance the count by 1

# check your code


# %%
###################################### Q5 ###############################
# A math question
# For a integer n, let us try to find all the factors and print them out
n = 1862

# pseudocode
# loop through an index i (from 1, not zero)
#   if n/i is integer, print i


#%%