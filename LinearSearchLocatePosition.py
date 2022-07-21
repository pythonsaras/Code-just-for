

# cards=[1,2,34,52,4,13]
# query=34
# def locate_position(cards,query):
#     for i in cards:
#        if  cards[i]==query:
#         return i+1
# position=locate_position(cards,query)
# print(f"Location of your query number {query} is {position}")
###################Test cases ########################
def locate_position(cards,query):
    position=0
    while position<len(cards):
       if cards[position]==query:
           return position
       position+=1
    return -1
list1=[]
for i in range(10000000):
    list1.append(i)
tests=[
    {'input':
    {
        'cards':[1,2,34,52,4,13],
        'query':13}
    ,'output':5},
    {'input':
    {
        'cards':[1,2,34,52,4,13],
        'query':34}
    ,'output':2},
    {'input':
    {
        'cards':[1,2,34,34,52,4,13],
        'query':1}
    ,'output':0},
    {'input':
    {
        'cards':[34],
        'query':34}
    ,'output':0},
    {'input':
    {
        'cards':[1,2,34,34,52,4,13],
        'query':3}
    ,'output':-1},
    {'input':
    {
        'cards':[1,1,2,2,34,34,43,34,34,34,34,52,4,13],
        'query':34}
    ,'output':4},
    # {'input':
    # {
    #     'cards':list1,
    #     'query':9999999}
    # ,'output':9999999},
     {'input':
    {
        'cards':[],
        'query':2}
    ,'output':-1}
     ]
# for test in tests:
#     print(test)
#     result=locate_position(**test['input'])
#     if result==test['output']:
#         print(f"Location of your query number {test['input']['query']} is {result}")
#         print("TEST PASSED")
#     else:
#         print("Wrong output")    
    
    
    
    
    
    
from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(locate_position,tests)