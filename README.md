# quiz03 (1)

def dot(vector01,vector02): 
  '''
This function takes two vectors (vector01 and vector02) as its arguments. It first checks if two vectors are the same size. If sizes are equal it then takes the dot product of two vectors then returns the result. if not it prints Error".
   '''
  result=0
  a=len(vector01)
  b=len(vector02)
  if (a!=b):
    # Here the fucntion checks if two vectors are the same size
    print ("Error")
    return None
  
  for i in range(len(vector01)):
    result=result+vector01[i]*vector02[i]
    # takes the dot product of two vectors
  return result
    #returns the dot product
vector1=[1,2,2]
vector2=[1,2,3]

vector3=[1,2]
vector4=[1,3,5]
print(dot(vector1,vector2))
# the test values wtih right and not right vector sizes are being checked.
#print(dot(vector3,vector4))

# quiz03 (2)

def vecSubtract(vector01,vector02): 
  '''
This function takes two vectors (vector01 and vector02) as its arguments. It first checks if two vectors are the same size. If sizes are equal it then subtracts vector02 from vector01,then returns the result which is vector. if not it prints Error".
   '''
  result=[]
  # assigning an empty list to get back a new vector after calculations
  a=len(vector01)
  b=len(vector02)
  if (a!=b):
    # Here the fucntion checks if two vectors are the same size
    print ("Error")
    return None
  
  for i in range(len(vector01)):
    total=0
    total+=vector01[i]-vector02[i]
    # vector subtraction
    result.append(total)
  return result
    #returns the new subtracted vector
vector1=[1,2,5]
vector2=[1,2,3]

vector3=[1,2]
vector4=[1,3,5]
print(vecSubtract(vector1,vector2))
# the test values wtih right and not right vector sizes are being checked.
#print(vecSubtract(vector3,vector4))
