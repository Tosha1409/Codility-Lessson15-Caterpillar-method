def solution(A):
    right=len(A)-1
    left=0
    count=len(A)
    
    while (right!=left):
        if abs(A[right])<abs(A[left]): 
            left +=1
            if A[left]==A[left-1]: count -= 1
        elif abs(A[right])>abs(A[left]): 
            right -=1
            if A[right]==A[right+1]: count -= 1
        elif abs(A[right])==abs(A[left]): 
            count -=1
            left +=1
    
    return(count)