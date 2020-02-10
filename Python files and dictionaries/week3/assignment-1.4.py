# Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(num_list):
    return(sum(num_list))
if __name__=="__main__":
    num_list=list(map(int,input().split()))
    print(accum(num_list))
