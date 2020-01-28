'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer. '''


fname=input("Enter the filename:")
fh=open(fname)
words=[]
for line in fh:
    line=line.rstrip()
    if not line.startswith("From: "):
        continue
    line=line.split()
    words.append(line[1])
data={}
for word in words:
    data[word]=data.get(word,0)+1
big_word=None
big_count=None
for mail,count in data.items():
    if big_count is None or count>big_count:
        big_count=count
        big_word=mail
print(big_word,big_count)
