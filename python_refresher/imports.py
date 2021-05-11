#import mymodule
#mymodule.divide(2,2)

from mymodule import divide

print(divide(10, 20))
print(__name__)


import sys

# Paths that python looks at to find imports
print(sys.path)


# Other versions of python require you to create
# an __init__.py file in your directories you want
# to import from.


print(sys.modules)
