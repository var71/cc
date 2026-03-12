from zeep import Client

client=Client('http://127.0.0.1:10000/?wsdl')

add=client.service.add(5,10)
sub=client.service.subtract(5,10)
mul=client.service.multiply(5,10)
square=client.service.square(5)

print('Addition: ',add)
print('Subtraction: ',sub)
print('Multiplication: ',mul)
print('Square: ',square)