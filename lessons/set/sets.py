empty_set = set()
A = {2, 3, 6, 8, 9, 9, 9, 11}
B = {3, 5, 6, 7, 8, 10}

#A N B = 3, 6, 8
#A U B = 2, 3, 5, 6, 7, 8, 9, 10, 11
#A \ B = 2, 9, 11
#B \ A = 5, 7, 10
#(A\B) U (B\A) = 2, 5, 7, 9, 10, 11

print(A)
print(len(A))
print(B)
print(len(B))

print(6 in A)
print(4 in B)

'''for item in A:
    print(item)'''

A.add(13)
A.add(45)
A.update([7, 15, 25, 40]) #can update set with multiple at a time
print(A) #random ordering compared to indexing seen in lists & removes duplicates


fruits = {'banana', 'strawberry', 'pineapple', 'blueberry', 'kiwi'}
vegetables = ('cabbage', 'carrot', 'celery', 'spinach', 'lettuce') #tuple
fruits.update(vegetables)
print(fruits)
print(vegetables) 

B.remove(5)
B.pop() #removes one random item (maybe last maybe not)
print(B)
print(B)

fruits = ['banana', 'strawberry', 'pineapple', 'blueberry', 'kiwi', 'banana']
print(fruits)
print(set(fruits))

print(A.union(B))
print(B.union(A))
print(B.intersection(A))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.isdisjoint(B))
