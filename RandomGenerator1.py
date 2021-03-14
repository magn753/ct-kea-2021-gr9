#import the Faker function in order for the randomiser to work
import random
import faker
import string

Denis = faker.Faker()
#randoming name
def FirstName():
    return Denis.name().split(" ")[0]
#randoming last name
def LastName():
    return Denis.name().split(" ")[-1]
#randoming studentID
def ID():
    return random.randint(10000, 99999)
#randoming phone
def Phone():
    return random.randint(10000000, 99999999)
#randoming Adress
def address():
    return Denis.address().split("\n")[0]
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
#randoming an email
def email():
    haha = random.randint(3,20)
    hihi = ["@gmail.com", "@hotmail.com", "@outlook.com", "@draven.com"]
    return random_char(haha)+hihi[random.randint(0,3)]
#randoming answer percentage value for design
def course():
    courses = ["0.0","6.66","13.33","20.0","26.66","33.33"]
    return courses[random.randint(0, 5)]
#randoming answer percentage value for DM
def course1():
    courses1 = ["0.0","6.66","13.33","20.0","26.66","33.33"]
    return courses1[random.randint(0, 5)]
#randoming answer percentage for the value of Development
def course2():
    courses2 = ["0.0","6.66","13.33","20.0","26.66","33.33"]
    return courses2[random.randint(0, 5)]
#adding all the values to the list
test = [ID(),FirstName(),LastName(),address(),email(),Phone(),float(course()),float(course1()),float(course2())]
#Calculating interest
p=(float(test[6]+test[7]+test[8]))
#calculating design to interest perceentage
g=(test[6]/p*100)
g = round(g, 2)
#calculating DM to interest perceentage
z=(test[7]/p*100)
z = round(z, 2)
#calculating Development to interest perceentage
v=(test[8]/p*100)
v = round(v, 2)
#adding new values to the end of the list
test.append(p)
test.append(g)
test.append(z)
test.append(v)
#printing the list
print(test)
