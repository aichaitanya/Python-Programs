class fifo:

    a = []
    
    def printstk(a):
        for i in a:
            print(i)
        
    def push(a):
        ele=int(input('Enter element : '))
        a.append(ele)
    
    def pop(a):
        if(top!=-1):
            print(a.pop(),'Popped')
        else : print('Stack Underflow')

    ch=1
    top=-1
    while(ch==1):
        print('1. Push 2. Pop 3. Print')
        op=int(input('Enter Option : '))
        if op==1:
            push(a)
            top+=1
        elif op==2:
            pop(a)
            top-=1
        elif op==3:
            printstk()
        else : print('Invalid')
        
        print('Current Stack : ')
        if top!=-1:
            printstk()
        else : print('Underflow')
        ch=int(input('Continue 1/0 : '))
        
        