# import ipaddress

# for i in range(1,10):
#     ad= ipaddress.ip_address(f'')
    

# import sys
# sys.argv
# if len(sys.argv) == 1:
#     print("Please enter an arguments")
# elif len(sys.argv) < 11:
#     left= 11 - len(sys.argv)
#     print(f'you have another {left} arguments')

#Page 200
# import os

# def see_folder(path):
    
#     if not os.path.exists(path):
#         print(f"Error: The path {path} does not exist")
#         return
    
#     if not os.path.isdir(path):
#         print(f"Error: the path {path} is not a directory ")
#         return
    
#     files = os.listdir(path)
    
#     if not files:
#         print(f"The directory {path} is empty")
#         return
    
#     print(f"Files in driectory {path}:")
    
#     for file in files:
        
#         full_path = os.path.join(path, file)
    
#         if os.path.isfile(full_path):
#             file_type = "File"
        
#         else:
#             file_type = "Directory"
            
#         print(f"  - {file} ({file_type})")
        
# see_folder(".")
        
        
        
# import os         
# def class_prac(one, two):
           
# parnet = (str(input"Insert a value for parnet folder name : \t  " ))
# child = (str(input "Insert a value for subfolder name: \t" ))

# parnet = os.path.join(one)
# child = os.path.join(two)   


# if parnet is None:
#     print (f"No path provided.")
#     return
  
# if os.path.exists(one):
#     print(f"The folder {one} exist. ")
#     return

# os.makedirs (parnet) and os.mkdir(child)


# class_prac 
        
        



import os

def class_prac(one=None, two=None):
    # Get input from user if parameters weren't provided
    if one is None:
        parent = str(input("Insert a value for parent folder name: \t"))
    else:
        parent = one
        
    if two is None:
        child = str(input("Insert a value for subfolder name: \t"))
    else:
        child = two
    
    # Check if parent parameter is empty
    if parent.strip() == "":
        print(f"No path provided for parent folder.")
        return
    
    # Create the full path for parent and child folders
    parent_path = os.path.join(os.getcwd(), parent)
    child_path = os.path.join(parent_path, child)
    
    # Check if the parent folder already exists
    if os.path.exists(parent_path):
        print(f"The folder {parent} already exists.")
        # We don't return here, we'll still try to create the child folder
    else:
        # Create the parent folder
        try:
            os.makedirs(parent_path)
            print(f"Created parent folder: {parent_path}")
        except Exception as e:
            print(f"Error creating parent folder: {e}")
            return
    
    # Check if the child folder already exists
    if os.path.exists(child_path):
        print(f"The subfolder {child} already exists.")
    else:
        # Create the child folder
        try:
            os.mkdir(child_path)
            print(f"Created subfolder: {child_path}")
        except Exception as e:
            print(f"Error creating subfolder: {e}")
    
# Call the function without arguments to trigger the input prompts
class_prac()
        
        
        
        