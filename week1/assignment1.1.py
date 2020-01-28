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
