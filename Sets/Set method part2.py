s1={1,2,3,4,4,93,23,12}
s2={1,3,4,34,76,98,123}
s1.discard(2)
print(s1)
s3=s1.intersection(s2);#return common value from s1 and s2
print(s3)

s1.intersection_update(s2)#s1 become Common value of s1 and s2
print(s1)

s=s1.isdisjoint(s2)
print(s)

s=s1.issubset(s2)
print(s)

s=s2.issuperset(s1)
print(s)

s2.pop()
print(s2)

s1.remove(3);#Discard is Better than remove Because Discard dont give Error when element is not Present but remove does
print(s1)

s4=s1.union(s2); #Join Two Sets
print(s4)
s1.update({5,7,9,34})
print(s1)
print(s2)
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
