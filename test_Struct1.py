from struct import *

#Store byte data

packed_data = pack('iif', 34, 65, 3.141)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('s'))
print(calcsize('iff'))

#To get bytes data to normal data.

original_data= unpack('iif', packed_data)
print(original_data)