s={1,2,3,34,3,5,5,46,46,4,6,54,4,56,546,4,64,45,4,54,5,4,54,5,45,4,5,4}#Doesnot Allow Any Duplicates
print(s)
print(1 in s)#Accesing Set Items
s2=s.copy()
print(s2)
s.add(9)
print(s)
s3=s.difference(s2)#return set only contain value exist in set1 and not in set2
print(s3)
s.difference_update(s2)#Only keep the difference set
print(s)
s.clear()
print(s)
