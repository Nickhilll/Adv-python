# simple interest calculation

def simple_interest(p, n, r):
    i = (p*n*r)/100
    amt = p+i
    return {'interest':i, 'amount': amt}

# Take input from users in console
p = float(input('please enter Principle in INR:'))
n = int(input('Please enter number of years :'))
r = float(input('Please enter rate of interest in  in %p/a:'))

# Calculate interest and amount
results = simple_interest(p, n, r)

#print the result
print(results)


    