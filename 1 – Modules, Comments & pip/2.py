# MODULES 
# A module is a file containing code written by somebody else (usually) which can be imported and used in our programs. 
# PIP 
# Pip is the package manager for python. You can use pip to install a module on your system. 
import pyjokes
print("Printing a joke:")
joke=pyjokes.get_joke()
print(joke)