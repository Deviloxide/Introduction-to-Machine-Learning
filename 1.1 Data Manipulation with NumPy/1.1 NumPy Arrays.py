import numpy as np

# Arrays
arr = np.array([[0, 1, 2], [3, 4, 5]], dtype=np.float32)
print(repr(arr))

arr2 = np.array([0, 0.1, 2])
print(repr(arr2))

print("\n")
# Copying
a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b)))

print("\n")
# Casting
arr = np.array([0, 1, 2])
print(arr.dtype)
arr = arr.astype(np.float32)
print(arr.dtype)

print("\n")
# NaN
arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# Will result in a ValueError
# np.array([np.nan, 1, 2], dtype=np.int32)

print("\n")
# Infinity
print(np.inf > 1000000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in an OverflowError
# np.array([np.inf, 3], dtype=np.int32)
