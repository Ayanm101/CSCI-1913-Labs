def left(e):
  return e[0]
def op(e):
  return e[1]
def right(e):
  return e[2]

def isInside(v,e):
  if type(e) == tuple: 
      if v == left(e):
          return True
      elif v == right(e):
          return True
      elif type(left(e)) == tuple:
          return isInside(v,left(e))
      elif type(right(e)) == tuple:
          return isInside(v,right(e))
      else:
          return False
  elif v == e:
     return True
  else:
     return False


def solve(v,q):
    if isInside(v,q[0]):
        return solving(v,q)
    elif isInside(v,q[2]):
        return solving (v,(q[2],q[1], q[0]))
    else:
        return None
        
def solving(v,q):
    if v == q[0]:
        return q
    elif q[0][1] == '+':
            return solvingAdd(v,q)
    elif q[0][1] == '-':
            return solvingSubtract(v,q)
    elif q[0][1] == '*':
            return solvingMultiply(v,q)
    elif q[0][1] == '/':
            return solvingDivide(v,q)
    else:
            return None



def solvingAdd(v,q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    
    if isInside(v, B):
      return solving(v, (B, '=', (C, '-', A)))
    else:
      return solving(v, (A, '=', (C, '-', B)))

def solvingSubtract(v,q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    
    if isInside(v, B):
      return solving(v, (B, '=', (A, '-', C)))
    else:
      return solving(v, (A, '=', (C, '+', B)))
      
def solvingMultiply(v,q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    
    if isInside(v, B):
      return solving(v, (B, '=', (C, '/', A)))
    else:
      return solving(v, (A, '=', (C, '/', B)))
      
def solvingDivide(v,q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    
    if isInside(v, B):
      return solving(v, (B, '=', (A, '/', C)))
    else:
      return solving(v, (A, '=', (C, '*', B)))
     
print(isInside ('x','x'))	
print(isInside ('x','y'))
print(isInside ('x', ('x', '+', 'y')))
print(isInside ('x', ('a', '+', 'b')))	
print(isInside ('+', ('a', '+', 'b')))
print(isInside ('x', (('m','*','x'), '+', 'b')))
print(solve('x', (('a', '+', 'x'), '=', 'c')))
#  ('x', '=', ('c', '-', 'a'))  2 points

print(solve('x', (('x', '+', 'b'), '=', 'c')))
#  ('x', '=', ('c', '-', 'b'))  2 points

print(solve('x', (('a', '-', 'x'), '=', 'c')))
#  ('x', '=', ('a', '-', 'c'))  2 points

print(solve('x', (('x', '-', 'b'), '=', 'c')))
#  ('x', '=', ('c', '+', 'b'))  2 points

print(solve('x', (('a', '*', 'x'), '=', 'c')))
#  ('x', '=', ('c', '/', 'a'))  2 points

print(solve('x', (('x', '*', 'b'), '=', 'c')))
#  ('x', '=', ('c', '/', 'b'))  2 points

print(solve('x', (('a', '/', 'x'), '=', 'c')))
#  ('x', '=', ('a', '/', 'c'))  2 points

print(solve('x', (('x', '/', 'b'), '=', 'c')))
#  ('x', '=', ('c', '*', 'b'))  2 points

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
# ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points
