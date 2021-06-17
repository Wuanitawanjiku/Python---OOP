#Given list x = [100,110,120,130,140,150], use list comprehension to create another list containing each number in the list multiplied by 5.
x = [100,110,120,130,140,150]
y = []
for i in x:
    print (i * 5)
    y.append(i)
    print(y)


#Write a function named divisible_by_three that accepts a number n and prints all numbers from 1 to n that are divisible by 3. 
def divisible_by_three(n):
    num_range = range(1, n)
    for a in num_range:
        if a % 3 == 0:
            return num_range
        else:
            return a
divisible_by_three(300)

#Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]
def flatten_list():
    lists = [[1,2],[3,4],[5,6]]
    list1 = [1,2]
    list2 = [1,2]
    list3 = [1,2]
    list4 = []
    lists = list1+list2+list3
    print(lists)
flatten_list()

#Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list.
def smallest(num):
    for n in num:
        return n
smallest(([3,6,8,2,4,1,5,7]))

#Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates
x = ['a','b','a','e','d','b','c','e','f','g','h']
def remove_duplicate(x):
    for letter in x:
        return letter
remove_duplicate(x)

#Write a function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.
def divisible_by_seven():
    num = range(100, 200)
    #list = []
    for n in num:
        if n % 7 == 0:
            return "Divisible"
        else:
            return num
divisible_by_seven()

#Given this list of students containing age and name,  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}],
#write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.
students = {"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"},
def greetings(students):
    for x in students:
        year = 2021 - students[x]
        return f"Hello {x}, you were born in the year {year}"
#greetings()

#Create a Class Rectangle with the following Attributes and Methods
#Attributes: The class has attributes width and length that represent the two sides of a rectangle 
#Methods:
#Add a method named area which returns the area (A) of the rectangle using the formula A=width*length
#Add a method named perimeter which returns the perimeter (P) of the rectangle using the formula P=2(length+width)

class Rectangle:    
    def __init__(self, width, length):
        self.width = width
        self.length = length  

    def area(self):
        A = self.width * self.length
        return f"A = {self.width}*{self.length}"

    def perimeter(self):
        P = self.width + self.length
        return f"P =2{self.length}+{self.width}"
        
