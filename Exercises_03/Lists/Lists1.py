#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: In this case, len returns the numbers of elements in the list, not the number of characters (for example, the number 10.13 would be a single element).

My_List = [1,2,3,4,"A"]
a = len(My_List)
print(a)
slice_1 = My_List[1:3:1]
print(slice_1)
My_character = My_List[-1]
print(My_character)
print("")
print("")

# Here i'm creating a list of data types, both string and int. I'm going to count the number of elements in the list.
List_of_DataTypes = ["A",2,"c",10,"Gh"]
b = len(List_of_DataTypes)
print(b)
slice_2 = List_of_DataTypes[0:6:2]
print(slice_2)
Characters = List_of_DataTypes[-2]
print(Characters)