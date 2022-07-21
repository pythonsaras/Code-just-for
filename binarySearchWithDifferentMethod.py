
list1=[]
for i in range(10000000):
    list1.append(i)
tests=[
    {'input':
    {
        'cards':[1,2,34,52,56,59],
        'query':59}
    ,'output':5},
    {'input':
    {
        'cards':[1,2,34,34,56,75,577],
        'query':34}
    ,'output':2},
    {'input':
    {
        'cards':[1,2,34,34,52],
        'query':1}
    ,'output':0},
    {'input':
    {
        'cards':[34],
        'query':34}
    ,'output':0},
    {'input':
    {
        'cards':[1,2,3,34,53,56,78,98],
        'query':98}
    ,'output':7},
    {'input':
    {
        'cards':[1,1,2,34,34,43],
        'query':34}
    ,'output':3},
    
    {'input':
    {
        'cards':[1,2,32,33,34,38,43,45],
        'query':34}
    ,'output':4},
    {'input':
    {
        'cards':list1,
        'query':9999999}
    ,'output':9999999},
     {'input':
    {
        'cards':[],
        'query':2}
    ,'output':-1}
     ]



def bineary_search(lo,hi,condition):
    while lo<=hi:
        mid=(lo+hi)//2
        result=condition(mid)
        print(f"Result found is {result}")
        if result=='found':
            return mid
        elif result=='left':
            hi=mid-1
        else:
            lo=mid+1
    return -1
def locate_card(cards,query):
    
    def condition(mid):
        mid_number=cards[mid]
        print(f"mid_number number is {mid_number}")
        print(f"mid value is {mid}")
        if mid_number==query:
            if mid-1>=0 and cards[mid-1]==query:
                return 'left'
            return 'found'
        elif mid_number>query:
            return 'left'
        else :
            return 'right'        
    return bineary_search(0,len(cards)-1,condition)     
# r=locate_card(cards=[1,2,3,4,5,6,7],query=6)
# print(r)

# for test in tests:
#     print(locate_card(test['input']['cards'],test['input']['query']))


# from jovian.pythondsa import evaluate_test_cases

# evaluate_test_cases(locate_card,tests)
