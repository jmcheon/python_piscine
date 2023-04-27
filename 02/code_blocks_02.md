
----

### # 02.00.00

```
list(ft_map(lambda x: x + 2, []))


```

----

### # 02.00.01

```
list(ft_map(lambda x: x + 2, [1]))


```

----

### # 02.00.02

```
list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5]))


```

----

### # 02.00.03

```
list(ft_filter(lambda x: x <= 1, []))


```

----

### # 02.00.04

```
ft_reduce((lambda x, y: x + y), [1])


```

----

### # 02.00.05

```
ft_reduce((lambda x, y: x * y), [1, 2, 3, 4])


```

----

### # 02.01.00

```
obj = what_are_the_vars(None)
doom_printer(obj)

# Shoud print:

# var_0: None
# end


```

----

### # 02.01.01

```
obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
doom_printer(obj)

# Shoud print:

# function: <function what_are_the_vars at 0x...>
# var_0: <function <lambda> at 0x...>
# end


```

----

### # 02.01.02

```
obj = what_are_the_vars(3, var_0=2)
doom_printer(obj)

# Shoud print:

# ERROR
# end


```

----

### # 02.03.00

```
from csvreader import CsvReader
import sys 

if __name__ == "__main__":
    filename = sys.argv[1]
    with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")

    with CsvReader(filename, header = True, skip_top=17, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")


```

----

### # 02.03.01

```
python main.py good.csv
# None
# [['Ruth', '       "F"', '   28', '       65', '      131']]

#['Name', '     "Sex"', ' "Age"', ' "Height (in)"', ' "Weight (lbs)"']
#[['Ruth', '       "F"', '   28', '       65', '      131']]


```

----

### # 02.03.02

```
python main.py bad.csv
# File is corrupted or missing


```

----

### # 02.03.03

```
python main.py unicorn.csv
# File is corrupted or missing


```

----

### # 02.04.00

```
find . -name "*.whl"
find . -name "*.tar.gz"


```

----

### # 02.04.01

```
python3 -m venv venv
source venv/bin/activate
bash build.sh


```

----

### # 02.04.02

```
pip list | grep minipack
# my-minipack        1.0.0


```

----

### # 02.04.03

```
import my_minipack.progressbar
import my_minipack.logger
```
