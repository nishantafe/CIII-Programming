# Create the following variables
birdtype = 10  # This variable contains a string value

''' We can combine a string literal with a variable which 
is also a string. This is called a concatenation. '''

# The print() has parameter sep and end.
# sep will change the default seperator (which is a space) into whatever your make it
# Example: sep="$" will make $ the seperator resulting in: How fast can an unladen$10$fly?
# The default value of end is a new line unless you clear it by doing end=""
print("How fast can an unladen", birdtype, "fly?", sep="$", end="")

