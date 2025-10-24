#File not found

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
   file = open("a_file.txt", "w")
   file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} is not present")

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("Something went wrong")




Height = float(input("Height: "))
Weight = int(input("Weight: "))

if Height > 3:
    raise ValueError("Human heights should not be over 3 meters")


bmi = Weight / (Height ** 2 )
print(bmi)