# data-structures
Repo that holds implementations of a variety of data structures

- Double-linked-list
- usage:
```
from dbl_lnk_lst import Dll

x = Dll([1,2,3])
```

methods:
push(val) will insert the value ‘val’ at the head of the list
append(val) will append the value ‘val’ at the tail of the list
pop() will pop the first value off the head of the list and return it.
shift() will remove the last value from the tail of the list and return it.
remove(val) will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.

### Credits:
- Thanks to [Tatiana](https://github.com/tanyaweaver) for helping with the push method on the doubly linked list!