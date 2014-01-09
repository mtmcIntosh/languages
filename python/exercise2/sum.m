infsum=(0);
row=1;
n=1;
arraySteps=zeros(100,2);
tol=1e-12;

denom=2^n;
infsum(row+1)=infsum(row) + 1/denom;

arraySteps(row+1,1) = n;
    
arraySteps(row+1,2) = infsum(row+1);

row=row+1;
n=n+1;
    

while infsum(row) > (infsum(row-1)+tol) || infsum(row) < (infsum(row-1)+tol);
    
    denom=2^n;
    
    infsum(row+1)=infsum(row)+ 1/denom;
    
    arraySteps(row+1,1) = n;
    
    arraySteps(row+1,2)= infsum(row+1);
    
    if infsum(row+1) < (infsum(row)+tol) && infsum(row+1) > (infsum(row)-tol);
        break;
    end
    
    n=n+1;
    row=row+1;
    
end
    
   
arraySteps