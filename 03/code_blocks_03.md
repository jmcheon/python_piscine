
----

### # 03.00.00

```
from NumPyCreator import NumPyCreator
npc = NumPyCreator()


```

----

### # 03.00.01

```
npc.from_list([[],[]])

# Shoud Output:

# array([], shape=(2, 0), dtype=float64)


```

----

### # 03.00.02

```
npc.from_list([[1,2,3],[6,3,4],[8,5,6]])

# Shoud Output:

# array([[1, 2, 3],
#       [6, 3, 4],
#       [8, 5, 6]])


```

----

### # 03.00.03

```
npc.from_tuple(("a","b","c"))

# Shoud Output:

# array(['a', 'b', 'c'], dtype='<U1')


```

----

### # 03.00.04

```
npc.from_iterable(range(5))

# Shoud Output:

# array([0, 1, 2, 3, 4])


```

----

### # 03.00.05

```
npc.from_shape((0, 0))

# Shoud Output:

# array([], shape=(0, 0), dtype=float64)


```

----

### # 03.00.06

```
npc.from_shape((3, 5))

# Should output:

# array([[0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0.]])


```

----

### # 03.00.07

```
npc.random((3, 5))

# Should output (*the values are random but the shape must be the same)*:   

# array([[0.74819604, 0.32295616, 0.27371925, 0.57171326, 0.92582071],
#       [0.70307642, 0.94846695, 0.12465384, 0.25146454, 0.11179953],
#       [0.38326719, 0.26179493, 0.88157011, 0.29978869, 0.72677049]])


```

----

### # 03.00.08

```
npc.identity(4)

# Should output:

# array([[1., 0., 0., 0.],
#       [0., 1., 0., 0.],
#       [0., 0., 1., 0.],
#       [0., 0., 0., 1.]])


```

----

### # 03.01.00

```
from ImageProcessor import ImageProcessor
imp = ImageProcessor()


```

----

### # 03.01.01

```
arr = imp.load("../ressources/42AI.png")
# Loading image of dimensions 200 x 200
print(arr)


```

----

### # 03.01.02

```
imp.display(arr)


```

----

### # 03.02.00

```
import numpy as np
from ScrapBooker import ScrapBooker
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
spb.crop(arr1, (3,1),(1,0))

# Output:

# array([[ 5],
#       [10],
#       [15]])


```

----

### # 03.02.01

```
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
spb.thin(arr2,3,0)

# Output :

# array([['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H'],
#         ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')


```

----

### # 03.02.02

```
arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
spb.thin(arr3,3,1)

# Output : 

# array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
#       ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
#       ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
#       ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
#       ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']], dtype='<U1')


```

----

### # 03.02.03

```
arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
spb.juxtapose(arr4, 2, 0)

# Output :

# array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9],
#       [1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])


```

----

### # 03.04.00

```
python Kmeans.py filepath='<path_to_solar_system_census_csv_file>' ncentroid=4 max_iter=30
```
