############################################
# THIS IS NOT A CLEANLY EXECUTEABLE FILE!! #
############################################
import csv
import sys
from PIL import Image
from PIL import ImageFilter

# open a file
### can read info from or write info to
### first argument is the filename
### second argument "w" means we plan to write to the file
### if the file does not exist, it will be automatically created
name = input("what's your name? ")
#file = open("names.txt", "w") #Dangerous. Recreates file w same name
#file = open("names.txt", "a")
with open("names.txt", "a") as file: #this automatically opens and closes file
    file.write(f"{name}\n")
# file.close() # Don't forget this step! Use keyword "with" instead


# read from a file
## argument "r" is the default so it isn't actually needed
with open("names.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print("hello, ", line.rstrip())


# better way to read and print sorted names from a file.
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# another way that sorts the file items
with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, ", line.rstrip())



# dealing with CSV files instead of .txt file
# Use the csv library to use reader, which interprets text to avoid
#  complexities in string interpretation
### Need to drop a hint in the first row to define columns in the .csv file (header)
students = []
with open("students.csv") as file:
    reader = csv.reader(file) #could also use csv.DictReader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

# lambda key word is in place of a nameless function (anonymous function)
### "key=" makes a call to a function
### since we would hypothetically call this funciton once, we skip defining it
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


# Writing to CSV files with csv library
name = input()
home = input()
with open("students.csv", "a") as file: # "a" argument is for append. Doesn't "restart" file
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) #can also use just "csv.writer(file)"
    writer.writerow({"name": name, "home": home})



# Using the library "Pillow", save an image to disk and make a gif with
images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
images[0].save(
    "pics.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)


with Image.open(arg) as image:
    print(image.size)
    print(image.format)
    image = image.rotate(180)
    image.save("out.jpeg")
    image.filter(ImageFilter.BLUR)
    image.save("blurry.jpeg")
