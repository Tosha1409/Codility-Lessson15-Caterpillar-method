def solution(A):
    A.sort()
    counter=0
    for x in range(0,len(A)-2):
        front=x+1
        for y in range (x+1, len(A)-1):
            if (A[x]+A[y]>A[front]): 
                for z in range (front+1, len(A)):
                    if ((A[x]+A[y]>A[z])): 
                        front=z
                        counter+=front-y
                    else: break
            elif (y+1==front): front +=1
            if front>=len(A)-1: break
    return(counter)