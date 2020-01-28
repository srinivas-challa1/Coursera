'''
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
'''
with open("travel_plans.txt","r") as trp:
    num=len(trp.read())
    print(num)

'''
We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
'''
with open("emotion_words.txt","r") as emotions:
    lines=emotions.readlines()
    num_words=0
    for line in lines:
        k=len(line.strip().split())
        num_words+=k
    print(num_words)

'''
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
'''
with open("school_prompt.txt","r") as school:
    lines=school.readlines()
    num_lines=len(lines)
    print(num_lines)

'''
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
'''

with open("school_prompt.txt","r") as school:
    school_data=school.read()
    beginning_chars=school_data[:30]
    print(beginning_chars)

'''
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
'''
with open("school_prompt.txt","r") as school:
    lines=school.readlines()
    three=[]
    for line in lines:
        line=line.strip().split()
        three.append(line[2])
print(three)

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
with open("emotion_words.txt","r") as emotional:
    lines=emotional.readlines()
    emotions=[]
    for line in lines:
        line=line.strip().split()
        emotions.append(line[0])
print(emotions)


#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars
with open("travel_plans.txt") as travel_plans:
    string=travel_plans.read()
    first_chars=string[:33]
    print(first_chars)
#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
with open("school_prompt.txt","r") as school:
    lines=school.readlines()
    p_words=[]
    for line in lines:
        line=line.strip().split()
        for word in line:
            if "p" in word:
                p_words.append(word)
print(p_words)
