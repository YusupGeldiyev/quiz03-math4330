# quiz03 (1)

def dot(vector01,vector02): 
  '''
This function takes two vectors (vector01 and vector02) as its arguments. It first checks if two vectors are the same size. 
If sizes are equal it then takes the dot product of two vectors then returns the result. if not it prints Error and returns none".
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
This function takes two vectors (vector01 and vector02) as its arguments. It first checks if two vectors are the same size. 
If sizes are equal it then subtracts vector02 from vector01,then returns the result which is vector. if not it prints Error retruns None".
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

# quiz03 (3)
def scalarVecMulti(scalar,vector): 
  '''
This function takes a scalar and a vector as its arguments. Then it multiplies scalar and a vector and returns the updated vector.
   '''
  result=[]
  # creating empty list to return the result after calculation so it puts back a new vector
  for i in range(len(vector)):
    total=0
    total=scalar*vector[i]
    # vector scalar multiplication
    result.append(total)
  return result
    #returns the new vector
scalar=2
vector2=[1,2,3]

vector3=[1,2]
vector4=[1,3,5]
print(scalarVecMulti(scalar,vector2))
# the test values wtih scalar and  different size vectors  are being checked.
#print(scalarVecMulti(vector3,vector4))

# quiz 03 (4)
def infNorm(vector):
  '''
  This function takes a vector as its arguments and returns the infinty norm of that vector.
  it takes the aboslute value of vector values and compares it to the assigned norm if its greater than that it returns the new norm
    '''
  norm=0
  for i in range(len(vector)):
  # take the lenthg of the vector
    if norm<=abs(vector[i]):
    #comparing absolute values of the vector to norm
      norm=abs(vector[i])
      #assinging new norm if its greater than exisiting norm
  return norm
vector1=[-3,4,-5]
test2=2
print(infNorm(vector1))
#print(infNorm(test2))

# quiz 03 (5)
def normalize(vector):
  '''
    This function takes a vector as its argument and returns the normalized vector with respect to infinty norm of that vector.
    it takes the aboslute value of vector values and compares it to the assigned norm if its greater than that it picks new biggest value in the list 
    it returns the new vector after its normalizeation the new given vecctor by dividing by infinity norm(whic is the new biggest value).
      '''
  norm=infNorm(vector)
  # function that calculates infinity norm is being assigned
  normalizedvector=[]
  #assigning empty list for new normalized vector
  for j in range(len(vector)):
    nvector=((1/norm))*vector[j]
    #dividing vector values by infinite norm
    normalizedvector.append(nvector)
  return normalizedvector
#returnig new normazlied vector with respect to infinity norm
vector1=[2,4,6]
test2=2
#testing valid and not valid inputs
print(normalize(vector1))
#print(normalize(test2))
