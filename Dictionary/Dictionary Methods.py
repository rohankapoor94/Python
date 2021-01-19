dic={"mobile phone":"iphone 12","Laptop":"Acer Nitro 5","Name":"Rohan Kapoor"};
print(dic["Laptop"]);
print(dic["Name"]);
print(dic["mobile phone"]);
key=[1,2,3,4];
value=["one ","two","three","four"];
co=dict(zip(key,value));
print(co)
co=dict(zip([1,2],["one","two"]));
print(co)

ro=dic.copy()
print(ro)

a=dic.fromkeys(key,5)#Give Multiple key a Single Value
print(a)

print(dic.get("Laptop"));
print(dic.items());
print(dic.keys());
print(dic.pop("mobile phone"))
print(dic)
print(dic.popitem())
print(dic)

print(co.setdefault(1,2))
print(co)

co.update({3:"three"})
print(co)
print(co.values())
