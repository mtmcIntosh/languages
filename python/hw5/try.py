missing_index=0
for cell in xrange(len(A)):
    if A[cell] == missing:
        if cell==0:
            A[cell]=A[cell+1]
        else:
            A[cell]=A[cell-1]
                
        missing_index=missing_index+1