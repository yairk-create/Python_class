

# class Bird:
#     def __init__(self, age, name):  # Corrected from __int__ to __init__
#         self.name = name
#         self.age = age 
    
#     def sound(self, wave):
#         print(f'Here comes the sound: {wave}')  # Also fixed a small typo in 'Here'

# # Create a Bird instance
# fly = Bird(69, "blue")

# # Now we can access attributes and methods
# print(f"Bird name: {fly.name}")
# print(f"Bird age: {fly.age}")
# fly.sound("Chirp chirp!")


import time 

seconds =  time.time()

time.ctime(seconds)

time.localtime(seconds)

import platform

platform.release()

platform.system()

platform.uname()