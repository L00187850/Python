#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: adding individual items to lists

# I added multiple items from one list to another using my_list.extend, essentially combining the lists
my_list = ["One","Two","Three"]
My_added_items = ["Five","Six","Seven"]
print(my_list)
my_list.append("Four")
print(my_list)
my_list.extend(My_added_items)
print(my_list)