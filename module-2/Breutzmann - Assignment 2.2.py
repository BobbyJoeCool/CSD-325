# Robert Breutzmann
# Module 11.2 Assignment - Used for Assignment 2.2 in CSD 325
# Due Date 10/26/2025

# Create a program with a recursive function that accepts an integer argument, n, and prints the number of 1 up to and including n. Then, write a non-recursive method that takes an integer argument, n, and prints the number of 1 up to and including n.


# While loop to get a valid input for "n"
while True:
    n = input("Please enter an integer greater than 0: ")
    try:
        n = int(n)
# Deliverable 2) Include test code that will not allow a negative or 0 value.
        if n <= 0: # Checks for an integer 0 or smaller
            print("Integers must be greater than 0.\n")
            continue
        else: # Breaks the While loop with a valid input for 'n'
            break
    except ValueError: #If n cannot be turned to an integer, prompt to try again.
        print("You did not enter a valid integer.  Please try again.\n")
        continue


# Deliverable 1) In your code documentation include an explanation of each functions approach to solving the problem.
'''
In this case, the recursive function takes the value for n and creates a value for 'current'
and assigns it 1.  The function then checks to see if 'n' is less than 'current', which would
be true when n is 0, and then prints the results and ends the function with an empty return statement.
If the number is 1 or larger, the function adds the current number of the 'current' variable (starting at one)
to the numberline list, then calls the recursion function again, but this time gives a value for the current
varriable as 'current+1' making it increase by one (this way it will go 1,2,3,4,5...)
If n is 5, the recursion function will run 6 times, adding 5 numbers to the numberline list.  
'''

def recursion(n, current=1): # Current is a running count of the number we are on, starting with 1.
    if current > n: # Base case will trigger when n is less than the current.
        print(", ".join(str(n) for n in numberline))
        return
    numberline.append(current)
    recursion(n, current +1)

# Deliverable 1) In your code documentation include an explanation of each functions approach to solving the problem.
'''
This method uses an iteration of a for loop for "i" in the range of 1 to n+1 
(the plus one so that) we get the last number to appear in the list.
Much like the recursive method, each time the the variable of the current number
(starting with 1) will be appended to the list numberline, and then it ends with
printing the numberline.
'''
def iteration(n):
    for i in range(1, n+1):
        numberline.append(i)
    print(", ".join(str(n) for n in numberline))


# Calls each function one by one. Refreshed the list numberline to empty before starting.
numberline=[]
print("\nStarting recursive function")
recursion(n)
print("Recursive function complete!")

numberline=[]
print("\nStarting iterative function")
iteration(n)
print("Iterative function complete!\n")

'''
the line that prints the numberline:
.join() joins the previous section ", " and the section following
which is a for loop that gets each number inside the number line 
one by one, so the output will be "1, 2, 3, 4, 5,... n".
'''