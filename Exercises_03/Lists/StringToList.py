#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: taking a string and making a list based off it.


# My Addition to the script is I added a second list, split it, and then combined it with the first list.
my_string = "12/9/22, 14:30, System Start, UB2204-Server"
list_of_values = my_string.split(",")
print(list_of_values)


My_string_2 = "14/11/24, 23:00, Script Written, Philip Stewart"
second_list_of_values = My_string_2.split(",")
print(second_list_of_values)
Extended_List = list_of_values.extend(second_list_of_values)
print(list_of_values)
