#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Loops are repeating code until a condition is met for them to break.



my_list = []
my_string = "Good Evening Everyone! How is everyone getting on!"
for letter in my_string:
    my_list.append(letter)

print(my_list)
print("")
print("")
print("")
print("")


my_list = [letter for letter in my_string]
print(my_list)

print("")
print("")
print("")
print("")

my_list1 = [number for number in range(0,10)]
print(my_list1)
print("")
print("")
print("")
print("")


my_list2 = [number * 5 for number in range(0,20)]
print(my_list2)
print("")
print("")
print("")
print("")

my_list = [number * 12 for number in range(0,20) if number < 10]
print(my_list)
print("")
print("")
print("")
print("")


# In my code for the Kelvin to Celsius to Fahrenheit conversion, I added [] or an empty list beside my celsius and fahrenheit variables. It basically means that i can add as much to the list as i want using append.
#I also used the append command to allow changes to be made to the empty list using "Temperature_in_Celsius.append(celsius). I then did the same for Fahrenheit.
# As a quick rule of thumb, we need to figure out how much kelvin is in 0 degrees celsius. After a quick research online, 273.15 Degrees Kelvin is 0 Degrees Celsius. 
# I have added this number and a few others which total to 100 Degrees Celsius
#The formula for Kelvin is "Kelvin = Celsius + 273.15". Celsius is "Kelvin - 273.15"
# 273.15 kelvin works out at 32 Fahrenheit which is 0 Celsius. the formula is "Fahrenheit = (Kelvin - 273.15) x 9/5 +32
#These are our set points.



# I just added this line below for myself. I personally operate better in celsius so I worked in tens.
   #Temperaturesincelsius=[0,       10      20      30      40      50     60     70      80      90}
Temperature_in_Kelvin = [273.15, 283.15, 293.15, 303.15, 313.15, 323.15, 333.15, 343.15, 353.15, 3633.15]
Temperature_in_Celsius = []
Temperature_in_fahrenheit = []

for temperature in Temperature_in_Kelvin:
    celsius = temperature - 273.15
    Temperature_in_Celsius.append(celsius)


for temperature in Temperature_in_Kelvin:
    fahrenheit = (temperature - 273.15) * 9/5 + 32
    
    Temperature_in_fahrenheit.append(fahrenheit)


print("Temperatures in Kelvin:", Temperature_in_Kelvin)
print("Converting Kelvin to Celsius:")
print("Temperatures in Celsius:", Temperature_in_Celsius)
print("Converting Celsius to Fahrenheit:")
print("Temperatures in Fahrenheit:", Temperature_in_fahrenheit)
