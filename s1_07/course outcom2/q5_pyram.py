def display():
    n=int(input("enter number of steps required"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j,end='')
        print(" ")
display()