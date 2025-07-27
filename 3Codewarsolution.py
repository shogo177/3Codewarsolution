#8 kyu / Even or Odd
#Python:
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else: 
        return "Odd"
    
    #8 kyu / Convert a Number to a String!
#Python:

def number_to_string(num):
    return str(num)

#8 kyu / Remove String Spaces
#Python:
def no_space(x):
    result = x.replace(' ', '')
    return result

print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))
print(no_space("8aaaaa dddd r     "))