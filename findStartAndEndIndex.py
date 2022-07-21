tests=[
    {'input':
    {
        'cards':[1,2,34,34,34,52,56,59],
        'query':34}
    ,'output':(2,4)}
    ]



def first_position(cards,query):
    
    def condition(mid):
        mid_number=cards[mid]
        if mid_number==query:
            if mid-1>=0 and cards[mid-1]==query:
                return 'left'
            return 'found'
        elif mid_number<query:
            return 'right'
        else :
            return 'left'        
    return bineary_search(0,len(cards)-1,condition)   
def last_position(cards,query):
    
    def condition(mid):
        mid_number=cards[mid]
        if mid_number==query:
            if mid-1>=0 and cards[mid+1]==query:
                return 'right'
            return 'found'
        elif mid_number<query:
            return 'right'
        else :
            return 'left'        
    return bineary_search(0,len(cards)-1,condition)        
def bineary_search(lo,hi,condition):
    while lo<=hi:
        mid=(lo+hi)//2
        result=condition(mid)
        if result=='found':
            return mid
        elif result=='left':
            hi=mid-1
        else:
            lo=mid+1
    return -1

def first_and_last_postion(cards,query):
    return first_position(cards,query),last_position(cards,query)



# from jovian.pythondsa import evaluate_test_cases

# evaluate_test_cases(first_and_last_postion,tests)



