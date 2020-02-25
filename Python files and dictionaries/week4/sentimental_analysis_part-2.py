import csv
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    for punctuation_char in punctuation_chars:
           string=string.replace(punctuation_char,"")
    return(string)
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(stringSentences):
    words=stringSentences.split()
    count=0
    for word in words:
        word=strip_punctuation(word.lower())
        for negative_word in negative_words:
            if(word==negative_word):
                count+=1
    return(count)
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(stringSentences):
    count=0
    strings=stringSentences.split()
    for word in strings:
        word=strip_punctuation(word.lower())
        for positive_word in positive_words:
            if word==positive_word:
                count+=1
    return(count)
ResultingFile=open("resulting_data.csv","w")
ResultingFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
ResultingFile.write("\n")
TwitterDataFile=open("project_twitter_data.csv","r")
lines=TwitterDataFile.readlines()
header=lines[0]
field_names=header.strip().split(",")
print(field_names)
for row in lines[1:]:
        values=row.strip().split(",")
        row_string="{},{},{},{},{}".format(values[1],values[2],get_pos(values[0]),get_neg(values[0]),get_pos(values[0])-get_neg(values[0]))
        ResultingFile.write(row_string)
        ResultingFile.write("\n")
ResultingFile.close()
with open("resulting_data.csv","r") as Result:
    csv_Reader=csv.reader(Result)
    for row in csv_Reader:
        print(row)
