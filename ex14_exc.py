# Simple exception example
# Syntax of try,except and finally blocks:

#try:
#   You do your operations here...
#   ...
#except ExceptionI:
#  If there is ExceptionI, then execute this block.
#except ExceptionII:
#   If there is ExceptionII, then execute this block.
#   ...
#else:
#   If there is no exception then execute this block. 


# Example 
# Defining two variables
x = 5
y = 0

# try, except and finally blocks below
try:
    z = x/y
    print(z)
except:
    print('divide by zero exception')
    
finally:
    print('All Done')