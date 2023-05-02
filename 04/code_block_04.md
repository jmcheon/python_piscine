
----

### # 04.00.00

```
from FileLoader import FileLoader
import os

f = FileLoader()

df = f.load(os.environ["CSV_PATH"])

# Should output (approximately) :

# (271116, 15) 


```

----

### # 04.00.01

```
f.display(df, 3)

# Should Output

#    ID                 Name Sex   Age  Height  Weight     Team  NOC        Games  Year  Season       City       Sport                         Event Medal
# 0   1            A Dijiang   M  24.0   180.0    80.0    China  CHN  1992 Summer  1992  Summer  Barcelona  Basketball   Basketball Men's Basketball   NaN
# 1   2             A Lamusi   M  23.0   170.0    60.0    China  CHN  2012 Summer  2012  Summer     London        Judo  Judo Men's Extra-Lightweight   NaN
# 2   3  Gunnar Nielsen Aaby   M  24.0     NaN     NaN  Denmark  DEN  1920 Summer  1920  Summer  Antwerpen    Football       Football Men's Football   NaN



```

----

### # 04.00.02

```
f.display(df, -3)

# Should output:

# ID                Name Sex   Age  Height  Weight    Team  NOC        Games  Year  Season            City        Sport                               Event Medal
# 271113  135570            Piotr ya   M  27.0   176.0    59.0  Poland  POL  2014 Winter  2014  Winter           Sochi  Ski Jumping  Ski Jumping Men's Large Hill, Team   NaN
# 271114  135571  Tomasz Ireneusz ya   M  30.0   185.0    96.0  Poland  POL  1998 Winter  1998  Winter          Nagano    Bobsleigh                Bobsleigh Men's Four   NaN
# 271115  135571  Tomasz Ireneusz ya   M  34.0   185.0    96.0  Poland  POL  2002 Winter  2002  Winter  Salt Lake City    Bobsleigh                Bobsleigh Men's Four   NaN


```

----

### # 04.00.03

```
f.display(df, 0)
# should display Nothing or the Header (column names of the dataframe)


```

----

### # 04.00.04

```
f.display(df, "lol")
#shouldnt crash


```

----

### # 04.01.00

```
from FileLoader import FileLoader
from YoungestFellah import youngestfellah
import os

loader = FileLoader()
data = loader.load(os.environ["CSV_PATH"])


print(youngestfellah(data, 1992))
# output is: "{'f': 12.0, 'm': 11.0}"

print(youngestfellah(data, 2004))
# output is: "{'f': 13.0, 'm': 14.0}"

print(youngestfellah(data, 2010))
# output is: "{'f': 15.0, 'm': 15.0}"

print(youngestfellah(data, 2003))
# output is: "{'f': nan, 'm': nan}"


```

----

### # 04.02.00

```
from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport
import os

loader = FileLoader()
data = loader.load(os.environ["CSV_PATH"])

print("")

print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n")
# output is "0.01935"

print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
# output is  "0.04127"

print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
# output is "0.00916"

```

----

### # 04.03.00

```
import pandas as pd
from HowManyMedals import how_many_medals
import os

data = pd.read_csv(os.environ["CSV_PATH"])

print(how_many_medals(data, 'Gary Abraham'))
#  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
#  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

print(how_many_medals(data, 'Kristin Otto'))
#  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"


```

----

### # 04.04.00

```
import pandas as pd
from SpationTemporalData import SpatioTemporalData
import os

df = pd.read_csv(os.environ["CSV_PATH"])
sp = SpatioTemporalData(df)

print(sp.where(2000))
# output is: ['Sydney']

print(sp.where(1980))
# output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.

print(sp.when('London'))
# output is: [2012, 1948, 1908]


```

----

### # 04.05.00

```
import pandas as pd
from HowManyMedalsByCountry import how_many_medals_by_country
import os

df = pd.read_csv(os.environ["CSV_PATH"])

print(how_many_medals_by_country(df, "United States") == {1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13}, 1904: {'G': 65, 'S': 68, 'B': 66}, 1906: {'G': 12, 'S': 6, 'B': 6}, 1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36}, 1920: {'G': 87, 'S': 41, 'B': 35}, 1924: {'G': 65, 'S': 41, 'B': 36}, 1928: {'G': 39, 'S': 22, 'B': 18}, 1932: {'G': 60, 'S': 57, 'B': 43}, 1936: {'G': 30, 'S': 29, 'B': 28}, 1948: {'G': 57, 'S': 34, 'B': 30}, 1952: {'G': 55, 'S': 38, 'B': 25}, 1956: {'G': 39, 'S': 57, 'B': 21}, 1960: {'G': 83, 'S': 27, 'B': 19}, 1964: {'G': 75, 'S': 36, 'B': 28}, 1968: {'G': 86, 'S': 36, 'B': 35}, 1972: {'G': 70, 'S': 58, 'B': 33}, 1976: {'G': 62, 'S': 46, 'B': 30}, 1980: {'G': 24, 'S': 4, 'B': 2}, 1984: {'G': 143, 'S': 75, 'B': 33}, 1988: {'G': 66, 'S': 48, 'B': 36}, 1992: {'G': 79, 'S': 46, 'B': 52}, 1994: {'G': 6, 'S': 8, 'B': 5}, 1996: {'G': 98, 'S': 41, 'B': 28}, 1998: {'G': 25, 'S': 2, 'B': 3}, 2000: {'G': 69, 'S': 34, 'B': 48}, 2002: {'G': 9, 'S': 52, 'B': 9}, 2004: {'G': 65, 'S': 66, 'B': 38}, 2006: {'G': 9, 'S': 7, 'B': 32}, 2008: {'G': 64, 'S': 61, 'B': 47}, 2010: {'G': 8, 'S': 61, 'B': 20}, 2012: {'G': 82, 'S': 44, 'B': 38}, 2014: {'G': 8, 'S': 28, 'B': 16}, 2016: {'G': 95, 'S': 52, 'B': 45}})

# Should output `True` 

# If the previous test fails the defendee should use the following list for team sports, If he does not filter for team sports, he failed the exercise.

team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
```
