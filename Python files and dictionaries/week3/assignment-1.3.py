'''
Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument
given, and returns that new string.
'''
def change(string):
    return("{}Nice to meet you!".format(string))
if __name__=="__main__":
    string=input()
    print(change(string))
