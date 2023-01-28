#This program calculates the factorial of a non negative number
#It can be done iteratively or recursively
#By Alex Thierry

#Recursive definition
def factorial_recusive(number):
    if number==0 or number==1:
        return 1              #0!=1 or 1!=1
    else:
        return number*factorial_recusive(number-1) #recursive call

#Iterative definition
def factorial_iterative(number):
    fact = 1
    for val in range(2,number+1):
        fact = fact * val           #performing the successive multiplication
    return fact


#main
if __name__ == '__main__':
    try:
        number = int(input('Enter the number you wish to calculate the factorial : ')) #getting number from user
        if number < 0:
            print('The factorial of a negative number does not exist.') #factorial of a number does not exist
        else:
            #factorial = factorial_iterative(number)
            factorial = factorial_recusive(number)
            print('The factorial of ',number,' is ',factorial,'.',sep='')
    except Exception as e:
        print('Something went wrong :',e)
