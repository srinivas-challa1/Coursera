'''
Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5,
return “Longer than 5”. If the length is less than 5, return “Less than 5”.
'''
def length(num_list):
    if len(num_list)>=5:
        return("Longer than 5")
    return("Less than 5")
if __name__=="__main__":
    num_list=list(map(int,input().split()))
    print(length(num_list))
    
