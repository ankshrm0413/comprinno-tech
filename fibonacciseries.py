#HERE IS THE IMPLEMENTATION OF ABOVE LOGIC USING PYTHON3.



#iterating till the range and taking the no of elements as input.
for i in range(int(input())):

# Reads the input from the user and store in the variable s
    s=input()
    
#creating a new dictionary.
    d={}
#executing the statement from the input which is stored in variable s.
    for i in s:
#executing the statement if it's satisfy then it will increment the the value of input and store on the empty disk.
        if(i in d):
            d[i]+=1 
        else:
#empty list obtain by adding the proceding terms.
            d[i]=1 
    l=[]
#if satisfy it will add the value of the terms 
    for i in d.values():
        l.append(i)
#this sort the values accordingly and update values
    l.sort()
#checks the value <3 if yes then it is dynamic or else it directly goes to the else part
    if(len(l)<3):
        print("Dynamic")
    else:
#checks the conditions is valid to implement the fibonacci series is its true and satisfy then its dynamic or else- else part is executed
    
        if(l[-1]==l[-2]+l[-3]):
            print("Dynamic")
        else:
            print("Not")
            