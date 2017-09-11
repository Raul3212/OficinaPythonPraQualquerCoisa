from mynode import *
from mystack import *
from myqueue import *
from mylist import *

def main():
    l = List()
    l.insert(10, 0)
    l.insert(3, 0)
    l.insert(2, 2)
    l.insert(5, 1)

    for i in range(len(l)):
        print(l[i])

    l.remove(2)

    for i in range(len(l)):
        print(l[i])

if __name__ == "__main__":
    main()