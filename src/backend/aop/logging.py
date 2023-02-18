import sys
import inspect





if __name__ == "__main__":
    print(sys.modules)
    for name, clazz in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        print(name, clazz)
