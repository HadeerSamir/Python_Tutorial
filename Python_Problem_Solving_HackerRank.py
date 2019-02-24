#String
########

def swap_case(s):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = []
    for i in range(len(s)):
        if s[i] in lower:
            t.append(s[i].upper())
        elif s[i] in upper:
            t.append(s[i].lower())
        else:
            t.append(s[i])

    return ''.join(t)

##########################################################################################################

def split_and_join(line):
    tokens= []
    tokens = line.split()
    sequences = "-".join(tokens)
    return sequences


###########################################################################################################

def print_full_name(a, b):
    print("Hello "+ a + " "+ b + "! You just delved into python.")

##############################################################################################################

def mutate_string(string, position, character):
    mutableString = list(string)
    mutableString[position] = character
    string = ''.join(mutableString)

    return string

########################################################################################################################
#Lists
########

if __name__ == '__main__':
    N = int(input())
    myList = []
    
    for i in range(N):
        lines = str(input()).split()
        if lines[0] == 'insert':
            myList.insert(int(lines[1]),int(lines[2]))
        elif lines[0] == 'print':
            print(myList)
        elif lines[0] == 'remove':
            myList.remove(int(lines[1]))
        elif lines[0] == 'append':
            myList.append(int(lines[1]))
        elif lines[0] == 'sort':
            myList.sort()
        elif lines[0] == 'pop':
            myList.pop()
        elif lines[0] == 'reverse':
            myList.reverse()

#############################################################################################################

s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))

#############################################################################################################

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

#################################################################################################################

def solve(s):
    names = s.split(' ')
    return ' '.join(name.capitalize() for name in names)

###################################################################################################################
# Leap Year 
#############

def is_leap(year):
    leap = True
    if year % 100 == 0:
        if year % 400 == 0:
            return leap
        else:
            return not(leap)

    if year % 4 == 0:
        return leap
    return not(leap)

#####################################################################################################################

#Print In One Line
####################

rom __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end="")

########################################################################################################################

# List Comprehensions
########################

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    ar=[]

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    ar.append([i,j,k])

    print(ar)
    
 ############################################################################################################################

# Runner_UP Score
#####################

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    max_score = arr[0]

    for i in arr[1:]:
        if i == max_score :
            continue
        else:
            print(i)
            break

###################################################################################################################

# Finding the percentage 
###########################
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total_sum=0.0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    for mark in student_marks[query_name]:
        total_sum+=mark
        

    average = total_sum/3
    
    print("%.2f" % average)    # round to 2 decimal numbers
   #######################################################################################################################

# Tuples
###########

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    thisTuple = tuple(integer_list)
    value = hash(thisTuple)
    print(value)
  
#####################################################################################################################
# Nested Lists
#################

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    scores = list(students[x][1] for x in range(len(students[0])))
    scores.sort()
   # min_score = scores[0]
   # second_min_score = 0

    '''for score in scores[1:]:
        if score == min_score:
            continue
        else:
            second_min_score = score
            break'''

    students = [x[0] for x in students if x[1] == scores[1]]
    students.sort()

    for j in students:
        print(j)
###########################################################################################################################

