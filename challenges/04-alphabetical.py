# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def sort(string):
    alpha_string = list(string)
    output = ''.join(sorted(alpha_string))
    print(f'sorted: {output}')


sort(string = input('anaconda:\n'))