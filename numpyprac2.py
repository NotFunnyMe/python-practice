import numpy as np

a = np.array([1,2,3])
print(a)
# Output: [1 2 3]

print(type(a))
print(a.shape)
print(a[0],a[1],a[2])

b = np.array([[3,4,5],[6,7,8]])
print(b)
print(b.shape)
c = np.zeros((2,2))
d = np.ones((2,2))
print(c)
print(d)
w = np.full((2,2),6)
print(w)
print(np.random.randint(1,10))

x = np.array([1.0,2.0])
print(x.dtype)
y = np.array([1,2],dtype=np.int64)
print(x.dtype)
q = np.array([[1,2],[3,4]],dtype=np.float64)
e = np.array([[5,6],[7,8]],dtype=np.float64)
print(q+e)
print(q)
print(e)
print(np.add(q,e))
print(q-e)
print(np.subtract(q,e))
print(q*e)
print(np.multiply(q,e))
print(q/e)
print(np.divide(q,e))
print(np.sqrt(q))
print(np.sqrt(e))
print(q.T)
print(np.sum(q))
print(np.mean(q,axis=0))
print(np.mean(q,axis=1))