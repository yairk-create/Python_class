#!/usr/bin/env python3

print("Hello-day" )

#print("HI, t, sep:"-")  


print("HI", "t", sep="-")


print("Yair", "kochavi", sep="n" )

#Practice page 36

my_name="yair"

my_age="36"

pet_name="bel"

print(my_name, my_age, pet_name, sep="\n")

##################################################################




#practice page 39

wife="moran"

print(wife)


_age_wife=31
f
print(type(wife))
print(type(_age_wife))

_age_wife = str(_age_wife)
print(type(_age_wife))

##############################################

#practice page 42




import socket

# Create a variable for the network you are connected to
network_name = "Kochavi"  # Replace with your actual network name

hostname= socket.gethostname()


print(hostname)

my_con = network_name + "-" +  hostname


connection_id = 2025

str_connection_id = str(connection_id)

my_con = str_connection_id + ":" + " " +  network_name +  "-" + hostname 

print(my_con)


###################################################
#practice page 49

name = input("plesae enter you name :" + " " )

print("\nHi:", name + " / ")


mood=input("How is the mood: " + " "  )

print(mood + " '' ")

locate =  mood.find("''")

print(locate)                    