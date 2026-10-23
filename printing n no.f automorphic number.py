for i in range(1,100):
    b=i
    c=i*i
    t=10
    while i>0:
        e=c%t
        if e == b:
            c=1
            break
        i=i//10
        t=t*10
    if c == 1:
        print(f"{b} is an automorphic number")
