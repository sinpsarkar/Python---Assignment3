# =============================================================================
# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()
# =============================================================================


def myreduce(function, sequence):
    res = sequence[0]
    for next in sequence[1:]:
        res = function(res, next)
    return res


# test myreduce function
in_list = [9,10,12,51]
myreduce( lambda x,y: x+y, in_list)


# =============================================================================
# 1.2 Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()
# =============================================================================

def myfilter(func, my_list):
    # Initialize empty list
    result = []# iterate over sequence of items in sequence and apply filter function
    for item in my_list:
        if func(item):
            result.append(item)
        # return funal output
    return result


# test myfilter function
def ispositive(x):
    if (x <= 0): 
        return False 
    else: 
        return True

in_list = [-1,6,-9,3]
test=myfilter(ispositive,in_list)
print(test)

in_list = [-1,6,-9,3]
test=myfilter(lambda x:x>=-2,in_list)
print(test)


# =============================================================================
# 2. Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# 
# =============================================================================


list1=[x for x in 'ACADGILD' if x !=" "]
print('List#1 : ',list1)

list2=[i*j for i in ('xyz') for j in range(1,5)]
print('List#2 : ',list2)


list3=[i*j for i in range(1,5) for j in('xyz')]
print('List#3 : ',list3)

list4=[[i+j] for i in range(1,4) for j in range(1,4)]
print('List#4 : ',list4)

list5=[[i+j for i in range(1,5)] for j in range(1,5)]
print('List#5 : ',list5)

list6=[(j,i) for i in  range(1,4) for j in range(1,4)]
print('List#6 : ',list6)
      

      
# =============================================================================
# 3. Implement a function longestWord() that takes a list of words and returns the longest one.
# =============================================================================

      
def longestWord(word_list):
    word_len = []
    for n in word_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

longestWord(['Institution', 'Information', 'Technology','Industry'])