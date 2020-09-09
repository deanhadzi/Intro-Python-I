"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for line in sys.argv:
    print(line)
print('----------\n')

# Print out the OS platform you're using:
print(sys.platform)
print('----------\n')

# Print out the version of Python you're using:
print(sys.version)
print('----------\n')

print(sys.version_info)
print('----------\n')


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getegid())
print(os.geteuid())
print(os.getgid())
print('----------\n')

# Print the current working directory (cwd):
print(os.getcwd())
print('----------\n')

# Print out your machine's login name
print(os.getlogin())
print('----------\n')
