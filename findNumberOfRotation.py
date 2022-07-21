

tests=[
    {'input':
    {
        'cards':[52,1,2,34,56,59],
        }
    ,'output':1},
    {'input':
    {
        'cards':[1,2,75,57,34,34,56],
        }
    ,'output':3},
    {'input':
    {
        'cards':[34,1,2,34,52],
    }
    ,'output':1},
    {'input':
    {
        'cards':[34],
        }
    ,'output':0},
    {'input':
    {
        'cards':[1,2,3,34,78,98,53,56],
        }
    ,'output':6},
    {'input':
    {
        'cards':[2,34,34,1,1,43],
        }
    ,'output':3},
    
    {'input':
    {
        'cards':[34,38,43,45,1,2,32,33],
        }
    ,'output':4},
     {'input':
    {
        'cards':[],
    }
    ,'output':0}
     ]

def count_rotation_linear(cards):
    position=0
    while position<len(cards):
        if position>0 and cards[position]<cards[position-1]:
            return position
        
        position+=1
    return 0

# for test in tests:
#     # print(test)
#     result=count_rotation_linear(test['input']['cards'])
#     if result==test['output']:
#         print(f"Rotation  is {result}")
#         print("TEST PASSED")
#     else:
#         print("Wrong output")    
    

from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(count_rotation_linear,tests)
    


