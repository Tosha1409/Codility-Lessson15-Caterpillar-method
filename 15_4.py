def solution(A):
    l=len(A)
    A.sort()
    back=0
    front=l-1
    result=max(abs(A[0]), abs(A[l-1]))*2
    while (front>=back):
        result = min(abs(A[front]+A[back]), result)
        if abs(A[front])>abs(A[back]):
            front -=1
        else:
            back +=1
                
    return(result)