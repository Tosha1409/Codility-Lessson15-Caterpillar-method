def solution(M, A):
    r=0
    counter=0
    check=[M+1]*(M+1)
    for back in range(0,len(A)):
        for front in range(back+r,len(A)):
            if (check[A[front]]<back) or (check[A[front]]>front):
                r += 1
                check[A[front]]=front
            else:
                break
        counter += r
        r -= 1  
    return (min((counter), 1000000000))