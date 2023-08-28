#python_small programs
prime_and_composite = lambda l: "Prime" if (len([z + 1 for i in range(1, l + 1) if l % i == 0]) == 2) else "Composite"

print( n, "is a ", pnc(n), "number")

#prime_number
user_ip = int(input("enter a number: "))
cnt = 0
test = lambda l: "Prime" if (len([cnt+1 for i in range(1, l+1) if l % i == 0]) == 2) else "Composite"
print(test(user_ip))

# lesser_of_two_evens
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        pass


#animal_crackers
#function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    if text.split(" ")[0][0] == text.split(" ")[1][0]:
        return True
    else:
        return False

#function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    string_list = [name.capitalize()[0:3], name[3:].capitalize()]
    return "".join(string_list)

#function when given a sentence, return a sentence with the words reversed
def master_yoda(text):
    return " ".join(text.split(" ")[::-1])

#function when given a sentence, return a sentence with the words reversed
sample = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(s):
    d = {"upper": 0, "lower": 0}
    for l in s:
        if l.isupper():
            d["upper"] += 1
        elif l.islower():
            d["lower"] += 1
        else:
            pass
    return d


print(up_low(sample))


#iven an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10


print(almost_there(50))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3, 3]:
            return True
    return False


print(has_33([3, 1, 3, 3]))

#function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    c, z = 0, 0
    pnc = lambda l: 1 if (len([z + 1 for i in range(1, l + 1) if l % i == 0]) == 2) else 0
    for n in range(0, num+1):
        c += pnc(n)

    return c


print(count_primes(100))

def up_low(s):
    dict_a = {'upper':0, 'lower':0}

    for chr in s:
        if chr.isupper():
            dict_a['upper'] += 1
        if chr.islower():
            dict_a['lower'] += 1
        else:
            pass

    return dict_a

print(up_low("ShaheJahan was a great man. He was a noble king of India."))


class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        #sqrt(((x_2-x_1)²+(y_2-y_1)²) )
        return round(((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5, 3)

    def slope(self):
        #(y_2-y_1)/(x_2-x_1)
        return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())




list_num = ['a', 'b', 2, 3, 2, 'a', 6, 6, 11, '%', '*', '%']
dup_list = []
cleaned_list = list_num

for i in list_num:
    if list_num.count(i) > 1 and i not in dup_list:
        dup_list.append(i)


for i in cleaned_list:
    if cleaned_list.count(i) > 1:
        cleaned_list.remove(i)



print(cleaned_list)


# find the first non-recurring element in a string
num_list = [1, 2, 3, 6, 7, 1, 3, 7, 8, 8, 9, 0, 3, 4, 5]
string_list = "kjdnfvniegbienvkfviuernvrenveir"

new_dict = {}
for i in string_list:
    if i in new_dict.keys():
        new_dict[i] += 1
    else:
        new_dict[i] = 1

key = [k for k, v in new_dict.items() if v == 1]
print(key[0])




