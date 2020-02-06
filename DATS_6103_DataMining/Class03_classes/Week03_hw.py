
###############  HW  Week03      HW  Week03      HW  Week03    ###############
# We first continue to complete the grade record that we were working on in class.
#%%

  

#%%
###################################### Q1 ###############################
# let us write a function find_grade(total) 
# which will take your course total (0-100), and output the letter grade (see your syllabus)
# have a habbit of putting in the docstring
total = 62.1

def find_grade(total):
  grade = 'A' if (total>=93) else 'A-' if (total>=90) else 'B+' if (total>=87) else 'B' if (total>=83) else 'B-' if (total>=80) else 'C+' if (total>=77) else 'C' if (total>=73) else 'C-' if (total>=70)else 'D' if (total>=60) else 'F'
  #print(grade)
  return grade 

# Try:
print(find_grade(total))

# What is the input (function argument) data type for total? 
print(type(total)) #float
# What is the output (function return) data type for find_grade(total) ?
print(type(grade)) #string


#%%
###################################### Q2 ###############################
# next the function to_gradepoint(grade)
# which convert a letter grade to a grade point. A is 4.0, A- is 3.7, etc
grade = 'C-'

def to_gradepoint(grade):
  gradepoint=4 if (grade=='A') else 3.7 if (grade=='A-') else 3.3 if (grade=='B+') else 3.0 if (grade=='B') else 2.7 if (grade=='B-') else 2.3 if (grade=='c+') else 2.0 if (grade=='C') else 1.7 if (grade=='C-') else 1.3 if (grade=='D+') else 1.0 if (grade=='D') else 0.7 if (grade=='D-') else 0
  # print(grade)
  return gradepoint

# Try:
print(to_gradepoint(grade))

# What is the input (function argument) data type for find_grade? 
print(type(grade)) #Answer is "string"
# What is the output (function return) data type for find_grade(grade) ?
#Answer is "float"


#%%
###################################### Q3 ###############################
# next the function to_gradepoint_credit(course)
# which calculates the total weight grade points you earned in one course. Say A- with 3 credits, that's 11.1 total grade_point_credit

course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'A-', "credits":3 } 

def to_gradepoint_credit(course):
  grade_point_credit= course['credits']*to_gradepoint(course['grade'])
  print(" %.2f" % grade_point_credit)
  return grade_point_credit

# Try:
print(" %.2f " % to_gradepoint_credit(course) )

# What is the input (function argument) data type for to_gradepoint_credit? 
print(type(course)) #Answer is "Dictionary"
# What is the output (function return) data type for to_gradepoint_credit(course) ?
print(type(to_gradepoint_credit(course))) 
#Answer is "float"


#%%
###################################### Q4 ###############################
# next the function gpa(courses) to calculate the GPA 
# It is acceptable syntax for list, dictionary, JSON and the likes to be spread over multiple lines.
courses = [ 
  { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } , 
  { "class":"Data Warehousing", "id":"DATS 6102", "semester":"fall", "year":2018, "grade":'A-', "credits":4 } , 
  { "class":"Intro Data Mining", "id":"DATS 6103", "semester":"spring", "year":2018, "grade":'A', "credits":3 } ,
  { "class":"Machine Learning I", "id":"DATS 6202", "semester":"fall", "year":2018, "grade":'B+', "credits":4 } , 
  { "class":"Machine Learning II", "id":"DATS 6203", "semester":"spring", "year":2019, "grade":'A-', "credits":4 } , 
  { "class":"Visualization", "id":"DATS 6401", "semester":"spring", "year":2019, "grade":'C+', "credits":3 } , 
  { "class":"Capstone", "id":"DATS 6101", "semester":"fall", "year":2019, "grade":'A-', "credits":3 } 
  ]

def find_gpa(courses):
  total_grade_point_credit =0
  total_credits =0
  for course in courses:
    #print(course)
    total_grade_point_credit += to_gradepoint_credit(course)
    total_credits += course["credits"]
    
    gpa=total_grade_point_credit/total_credits
    print(gpa)
  return gpa

# Try:
print(" %.2f " % find_gpa(courses) )

# What is the input (function argument) data type for find_gpa? 
print(type(courses)) #Answer is "list"
# What is the output (function return) data type for find_gpa(courses) ?
print(type(find_gpa(courses))) #Answer is "Float"


#%%
###################################### Q5 ###############################
# Write a function to print out a grade record for a single class. 
# The return statement for such functions should be None or just blank
# while during the function call, it will display the print.
course = { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def printCourseRecord(course):
# write an appropriate and helpful docstring
# use a single print() statement to print out a line of info as shown here
#2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
# ??????    fill in your codes here
  Course_record = course['credits']*to_gradepoint(course['grade'])
  print(course['year'], course['semester'], "-", course['id'], ":", course['class'], '(', course['credits'], "credits",  ')', course['grade'], "Grade point credits:", " %.2f" % Course_record)
  return 

# Try:
printCourseRecord(course)

# What is the input (function argument) data type for printCourseRecord? 
print(type(course)) #Answer is Dictionary
# What is the output (function return) data type for printCourseRecord(course) ?
#Answer is list


#%%
###################################### Q6 ###############################
# write a function (with arguement of courses) to print out the complete transcript and the gpa at the end
# 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
# 2018 fall - DATS 6102 : Data Warehousing (4 credits) A-  Grade point credits: 14.80 
# ........  few more lines
# Cumulative GPA: ?????

# write a function (with arguement of courses) to print out the complete transcript and the gpa at the end

# 2018 spring - DATS 6101 : Intro to DS (3 credits) B- Grade point credits: 8.10

# 2018 fall - DATS 6102 : Data Warehousing (4 credits) A- Grade point credits: 14.80

# ........ few more lines

# Cumulative GPA: ?????

courses = [ 
  { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } , 
  { "class":"Data Warehousing", "id":"DATS 6102", "semester":"fall", "year":2018, "grade":'A-', "credits":4 } , 
  { "class":"Intro Data Mining", "id":"DATS 6103", "semester":"spring", "year":2018, "grade":'A', "credits":3 } ,
  { "class":"Machine Learning I", "id":"DATS 6202", "semester":"fall", "year":2018, "grade":'B+', "credits":4 } , 
  { "class":"Machine Learning II", "id":"DATS 6203", "semester":"spring", "year":2019, "grade":'A-', "credits":4 } , 
  { "class":"Visualization", "id":"DATS 6401", "semester":"spring", "year":2019, "grade":'C+', "credits":3 } , 
  { "class":"Capstone", "id":"DATS 6101", "semester":"fall", "year":2019, "grade":'A-', "credits":3 } 
  ]

def printTranscript(courses):
  grades = {'A':4, 'A-':3.7, 'B+':3.3, 'B':3, 'B-':2.7, 'C+':2.3, 'C':2, 'C-':1.7, 'D+':1.3, 'D':1, 'D-':0.7, 'F':0}
  total_gpa = 0
  total_creds = 0
  for course in courses:
    gpa = (course['credits']*grades[course['grade']])
    total_gpa += gpa
    total_creds += course['credits']
    print(str(course['year'])+" "+course['semester']+" - "+course['id']+" : "+course['class']+" ("+str(course['credits'])+" credits) "+course['grade']+" Grade point credits: "+("%.2f"%gpa))
    print("Cumulative GPA: "+str((total_gpa/total_creds)*1))
  return # or return None
  
printTranscript(courses)


# What is the input (function argument) data type for printTranscript? 
print(type(courses)) #Answer is list
# What is the output (function return) data type for printTranscript(courses) ?
#Answer is string # becuase of print("Cumulative GPA: "+str((total_gpa/total_creds)*1)) # str function is converting the numbers to a string


#%% 
# ######  QUESTION 7   Recursive function   ##########
# Write a recursive function that calculates the Fibonancci sequence.
# The recusive relation is fib(n) = fib(n-1) + fib(n-2), 
# and the typically choice of seed values are fib(0) = 0, fib(1) = 1. 
# From there, we can build fib(2) and onwards to be 
# fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5, fib(6)=8, fib(7)=13, ...
# Let's set it up from here:

def fib(n):
    if(n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2))

# Try
print(fib(6))  #should gives 8
print(fib(7))  #should gives 13




#%%

