#Ayan Mohamed

class Zillion:
 
   def __init__(self, digits): 
      self.digits=digits
      self.lists=[]
      
    
      for n in digits:  
         if n <='9' and n >= '0':
               self.lists += [int(n)]
         elif n not in (' ', ','):
               raise RuntimeError
      if len(self.lists) == 0: 
            raise RuntimeError
      
            
   def increment(self):
      initial=-1
      cond1=True
      count=0
      while cond1:
         if self.lists[initial] == 9:
            self.lists[initial] = 0
            initial -=1
            count+=1
         else:
            self.lists[initial]+=1
            cond1=False
         if count==len(self.lists): 
            cond1=False
      if len(self.lists) == count:
         self.lists.insert(0,1)
         
   def isZero(self):
      possibility2 = True
      for i in range(0, len(self.lists)):
         if self.lists[i] != 0:
            possibility2 = False
      if possibility2 == True:
         return True
      else:
         return False

   def toString(self):
      newString=''
      for i in range(0, len(self.lists)):
         newString += str(self.lists[i])

      return newString

###############################################


#########  TESTS :)  ############################


###############################################

try:
  z = Zillion('')
except RuntimeError:
  print('Empty string')

# It must print 'Empty string' without apostrophes. 2 points.

try:
  z = Zillion(' , ')
except RuntimeError:
  print('No digits in the string')

# It must print 'No digits in the string' without apostrophes. 2 points.

try:
  z = Zillion('1+0')
except RuntimeError:
  print('Non-digit in the string')

# It must print 'Non-digit in the string' without apostrophes. 2 points.

try:
  z = Zillion('0')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000000000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('000 000 000')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
  z = Zillion('997')
except RuntimeError:
  print('This must not be printed')

#  It must print nothing.  2 points.

print(z.isZero())    #  It must print False. 2 points.

print(z.toString())  #  It must print 997. 2 points.

z.increment()

print(z.toString())  #  It must print 998. 2 points.

z.increment()

print(z.toString())  #  It must print 999. 2 points.

z.increment()

print(z.toString())  #  It must print 1000. 2 points.

try:
  z = Zillion('0 9,9 9')
except:
  print('This must not be printed')

#  It must print nothing.  3 points.

z.increment()
print(z.toString())  #  It must print 1000. 2 points.
