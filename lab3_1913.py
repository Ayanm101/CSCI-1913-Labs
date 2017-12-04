def most(P,s):
		
	if len(s) == 0:
		return False
	if int in s  == odd(N): 
		return False
	elif s[-1] % 2 == 0:
		return False
	else:
		return True
				
def sigma(F,B,E):
	
	
	a = range(B,E+1)   
	def sqr(x):             
		return x*x      
 
	def sum(x,y):            
		return x+y     
 
	if B > E:
		return 0
	else:
		squares = map(sqr, a)     
		sum_of_squares = reduce(sum, squares)
		return sum_of_squares 
  
 
#  ODD. Assume N is an integer. Test if N is odd.

def odd(N):
  return N % 2 != 0


print(most(odd, []))         #  False    2 points
print(most(odd, [0]))        #  False    2 points
print(most(odd, [1]))        #  True     2 points
print(most(odd, [1,2]))     #  False    2 points
print(most(odd, [1, 2, 3]))  #  True     2 points

#  SQR. Assume N is a number. Return N times N.

def sqr(N):
  return N * N

print(sigma(sqr, 0, 0))    #  0          2 points
print(sigma(sqr, 1, 0))    #  0          2 points
print(sigma(sqr, 0, 4))    #  30         2 points
print(sigma(sqr, 1, 1))    #  1          2 points
print(sigma(sqr, 2, 100))  #  338349     2 points
