def pure_add(a,b):
    return a+b
print(pure_add(40,90))



counter = 0
def impure_increment():
    global counter
    counter+=10
    return counter
print(impure_increment())


def factorial_recursive(n):
    if (n==0) or (n==1):
        return 1
    return n*factorial_recursive(n-1)
print(factorial_recursive(5))



def square_list(nums):
    return list(map(lambda s:s**2,nums))
nums = [1,2,3,4,5,6,7,8,9]
print(square_list(nums))