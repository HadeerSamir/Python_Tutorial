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
