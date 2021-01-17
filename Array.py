array=[1,2,3,4,5];
print(array[:]);
array.append(4);
print(array[:]);
x=array.copy();
print(x)#Copied Array
print(array.count(4));#Count Elememt in Array
array.extend(x)
print(array);
x.insert(0,9);
print(x);
print(x.index(9));
print(x.pop());
print(x)
x.remove(2);
print(x)
x.clear();
print(x)
print(x[:]);
array.sort();
print(array)
array.reverse();
print(array)
print(min(array))
print(max(array))
del array[0:9]
print(array)
