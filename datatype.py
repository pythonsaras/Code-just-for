# new data type 
# from collections import namedtuple
# a=namedtuple('coures','name,technology')
# s=a('data science','python')
# print(s)
# s=a._make(['AI','Python'])
# print(s)


# # It use to insert and delete the data
# from collections import deque

# a=['a','b','c']
# d=deque(a)
# print(d)
# d.append('python')
# d.appendleft('hello')
# print(d)
# d.pop()
# d.popleft()
# print(d)
# # single view of maltipule mapping
# from collections import ChainMap
# a={1:'hello',2:'Sir'} 
# b={3:'hy'}
# c=ChainMap(a,b)
# print(c)

# # count hash object or repeted value

# from collections import Counter
# a=[1,2,1,2,3,2,3,1,2,3,43,5]
# c=Counter(a)
# print(c)
# print(list(c.elements()))

# print(c.most_common())
# sub={2:1}
# print(c.subtract(sub))
# print(c.most_common())

from collections import OrderedDict,defaultdict
# d=OrderedDict()
# d[1]={1:'hello',2:'Sir'} 
# d[2]={3:'hy'}
# print(d)

# d=defaultdict(dict)
# d[1]={1:'hello',2:'Sir'} 
# d[2]={3:'hy'}
# print(d)
# print(d.keys())

