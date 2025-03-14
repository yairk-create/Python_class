# import ipaddress

# for i in range(1,10):
#     ad= ipaddress.ip_address(f'')
    

import sys
sys.argv
if len(sys.argv) == 1:
    print("Please enter an arguments")
elif len(sys.argv) < 11:
    left= 11 - len(sys.argv)
    print(f'you have another {left} arguments')

