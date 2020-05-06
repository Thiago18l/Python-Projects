a = '123'

# testing the type of variables

print(type(a))

b = 123

print(type(b))

i = '7'

if isinstance(i, int):
    i += 1
    print("Output in int case:", i)
elif isinstance(i, str):
    i = int(i)
    i += 1
    print("Output in str case:", i)

n = None
if n is None:
    print('Not suprise, I just defined n as None: ', n)


# casting between datatypes

string = '123'
b = int(string)
print("My new Integer: ", b)

string = '123.123'
b = float(string)
print("My new Float number: ", b)