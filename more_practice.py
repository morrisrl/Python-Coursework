#3.19 Assume a,b, and c have been defined in the interactive shell as shown
a, b, c = 3, 4, 5

#Within the interactive shell, write if statements that print 'OK' if:

#(a) a is less than b

if a < b:
    print("OK")

else:
    print("NOT OK")

#(b) c is less than b

if c < b:
    print("OK")

else:
    print("NOT OK")

#(c) The sum of a and b is equal to c.

if a + b == c:
    print("OK")

else:
    print("NOT OK")

#(d) The sum of the squares a and b is equal to c squared.

if a**2 + b**2 == c**2:
    print("OK")
    
else:
    print("NOT OK")

#3.24 Implement a program that requests a list of words from the user and then prints each word in the list that is not 'secret'.

words=input("Enter a list of words. ")
secret_word=["secret"]
for word in list(words):
	if word in secret_word:
		print(words.remove(word))


#3.30 Request four numbers, compute average of first 3 numbers, compare to last number

first_number=eval(input("Enter first number: "))
second_number=eval(input("Enter second number: "))
third_number=eval(input("Enter third number: "))
last_number=eval(input("Enter last number: "))

average=(first_number+second_number+third_number)/3
if average==last_number:
    print("Equal")
else:
    print("Not equal")

#3.34 Function pay() that takes as input 2 arguments: hourly wage and number of hours an employee worked

def pay(wage, hours):
    salary = wage*hours
    if hours > 40:
        overtime = hours - 40
        salary+= overtime * 1.5
    return salary
