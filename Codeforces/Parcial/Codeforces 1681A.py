for _ in range(int(input())):
    n=input()
    a=[*map(int,input().split())]
    m=input()
    b=[*map(int,input().split())]
    print(['Bob','Alice'][max(a)>=max(b)])
    print(['Bob','Alice'][max(a)>max(b)])