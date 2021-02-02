class lifo:
    class queue:
        def __init__(self):
            self.item=[]
            
        def empty(self):
            return self.item==[]
        def enque(self):
            a=int(input('Enter Element : '))
            self.item.append(a)
            print(self.item)
        def deque(self):
            if self.empty():
                print('Queue Underflow')
            else : print('Dequeued : ',self.item.pop(0))
            print(self.item)
        def prinq(self):
            print(self.item)
            
    q=queue()
    
    c=1
            
    while(c==1):
        print('1.Insert 2. Remove 3. Print')
        op=int(input('Enter Option : '))
        if op==1:
            q.enque()
        elif op==2:
            if q.empty():
                print('Underflow')
            else : q.deque()
        elif op==3:
            if q.empty():
                print('Underflow')
            else : q.prinq()
        else : print('Invalid')
        
        c=int(input('Continue 1/0 : '))
    