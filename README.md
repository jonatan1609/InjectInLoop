## InjectInLoop
##### This module that I created for fun, lets you inject function calls inside the loop itself, between every iteration.

### Important! currently, it only supports one-line for loop (only the "signature"), i.e.

```python
for XYZ().xyz in obj([], [], []):
```
will work, and 
```python
for XYZ().xyz in obj(
        [],
        [],
        []
):
```
Will not!


### Usage:

- import `inject_in_loop.Base` and inherit it with your own class.
- The inheriting class **must** define an attribute/method named `function` that will be called between each iteration.
- use the following syntax:
> `for YourClass().item in Array:...`

> `for YourClass().item1.item2 in Array:...`

>`for YourClass().item1, YourClass().item2 in Array:...`

>`for YourClass().item1, item2 in Array:...`

- In the first scenario, the variable `item` will be available.
- In the second scenario, the variables `item1` and `item2` will be available, It will only work in case that each element in the array can be unpacked into a two-items tuple, just like the regular `for a,b in array:...`
- In the third scenario, the variables `item1` and `item2` will be available, just like the second example. However, In this scenario `YourClass.function` will be called two times per each iteration, since there are two objects in that example.
- In the fourth scenario, the variables `item1` and `item2` will be available, like the second example, in fact it is the same as the second scenario.

You can also pass arguments to the class which will be sent into `function`:

an example from `inject_in_loop/main.py`:

```python
from inject_in_loop import Base
from time import sleep


class Sleep(Base):
    function = sleep


for Sleep(0.3).range1.range2 in zip(range(10), range(10)):
    print(range1 + range2, "[obj.a.b] a + b")
```

It will sleep 0.3 seconds between each iteration, and the output will be:
```
0 [obj.a.b] a + b
2 [obj.a.b] a + b
4 [obj.a.b] a + b
6 [obj.a.b] a + b
8 [obj.a.b] a + b
10 [obj.a.b] a + b
12 [obj.a.b] a + b
14 [obj.a.b] a + b
16 [obj.a.b] a + b
18 [obj.a.b] a + b
```
or:

```python
class PrintNewLine(Base):
    function = print


for PrintNewLine().item in ("a", "b", "c"):
    print(item)
```

The output will be
```
a

b

c
```


You can see a couple of examples in `inject_in_loop/main.py`.
> In order to run those examples you need to run that file directly (not by importing it.).

You can also create mixins, which will call several functions with their corresponding arguments, as in the ex example:
```python
from inject_in_loop import Base
from time import sleep

class Mixin(Base):
    functions = [sleep, print]

for Mixin(f_params={"sleep": (1,),"print": ()}).element in range(10):
    print(element)
```
You must specify the parameter  `f_params` (must be a keyword argument) which will hold a dict with the corresponding tuple of arguments for each function.
the functions in a mixin will be held under an attribute named `functions` in the class.

You can also use unpacking in the for loop, as in the example:

```python
from inject_in_loop import Base
from time import sleep

class Sleep(Base):
    function = sleep
    
    
for Sleep(0.3, unpack="b").a.b.c in [["a", "b", "c", "d"]]*5:
    print(a, b, c)
```
The result will be:
```
a ['b', 'c'] d
a ['b', 'c'] d
a ['b', 'c'] d
a ['b', 'c'] d
a ['b', 'c'] d
```
`b` is the "starred" argument, as in the expression `a, *b, c = ["a", "b", "c", "d"]`.
You can't have more than one starred argument.
