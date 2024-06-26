def root_finder(a, b=1e-7,c = 100):
    if a < 0 :
        raise ValueError('Negative Number Do Not Have Square Root In Real Numbers.')
    elif a == 1:
        root = 1
        print('The Square Root is 1.')
    elif a == 0:
        root = 0
        print('The Square Root is 0.')
    else:
        low = 0
        high = max(1,a)
        root = None
        for _ in range(c):
            mid = (low+high)/2
            square_mid = mid**2
            if abs(square_mid-a) < b:
                root = mid
                break
            elif square_mid < a :
                low = mid
            else:
                high = mid
    return (root)

def call_root():
    a = float(input('Enter Your Number:\n '))
    print(f'The Square Root Of The Given Number Is:\n {root_finder(a)}\n')
    print('Thank You For Using The Program. Hope You Liked Our Program.')
    
call_root()
    
    