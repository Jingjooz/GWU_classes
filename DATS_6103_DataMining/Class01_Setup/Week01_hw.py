#%%[markdown]
# Question 1: Create a Markdown cell with the followings:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website 
# that you want us to see. Can be about yourself, or something you like.

# # About myself
#
# I am Sanhanat Satetasakdasiri. 
# I come from Bangkok, Thailand. 
# I am studing MA in Economics and Graduate Certificate in Data Science programs
# I plan to complete both programs in spring 2020
#
# Before I came Washingtion D.C., I worked as Economist at Ministry of Finance of Thailand.
# I took responbility to monitor Thai economic situation.
# Then, I achieved the Royal Thai government scholarship for master degree. That is why I am here.
# please contact me at [link](https://www.facebook.com/Jingjooz).

#%%
# Question 2: Follow our InClass01.py python file, create
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.

# list / array
alist = ['Introduction to Data Science','Data Warehousing','Introduction to Data Mining','Data Science Capstone','Machine Learning I: Algorithm Analysis','Visualization of Complex Data']
print (alist[-1])

#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in python here.

alist = ['Introduction to Data Science','Data Warehousing','Introduction to Data Mining','Data Science Capstone','Machine Learning I: Algorithm Analysis','Visualization of Complex Data']
alist[2] = "Introduction to Coal Mining"
print (alist)

#%%
# Question 4: Before you go see your acadmic advisor, you are 
# asked to create a python dictionary of the classes you plan to take, 
# with the course number as key. Please do that. Don't forget that your advisor 
# probably doesn't like coal. And that coal mining class doesn't even have a 
# course number.

adictionary = { "DATS6101":"Introduction to Data Science", "DATS6102":"Data Warehousing","":"Introduction to Coal Mining","DATS6501":"Data Science Capstone","DATS6202":"Machine Learning I: Algorithm Analysis","DATS6401":"Visualization of Complex Data"}
print(adictionary)

#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.

print(alist)
print(adictionary)
print(len(adictionary))
