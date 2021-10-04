i=1
sum = 0
while i <= 10:
    sum += i**2
    print(i, "\t", i**2, "\t", sum, "\t", i*(i+1)*(2*i +1)//6)
    i+=1