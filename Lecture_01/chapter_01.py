# mutable -> which we can change that is mutable
# immutable -> which we cannot change that is immutable

# For example ->

# mutable
num = 12;
print("Number is1 ", id(num));
num = 14;
print("Number is2 ", id(num));

#immutable -> As you can see the id of list is same even after appending an element
list1 = [1, 2, 3];
print("List is1 ", id(list1));
list1.append(4);
print("List is2 ", id(list1));