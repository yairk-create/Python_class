
mkdir py_env
 
 sudo apt install python3-venv -y    #installing the vrtual python envierment  very minimliast

 python3 -m venv py_env/   #confugring the virtual env folder

 source py_env/bin/activate


   pip freeze   # showing all the packages installed
   pip freeze > requiermetns.txt



poetry # another virtual tool the moset extended can test allso the app

#####################################
pipenv # a virtual tools 
mkdir for pipenv
in the directory
pipenvshell #to create a shell for it 
pipenv install flask # installing the python libraries on teh env from everywhere 
pipfile # the file where all the conf is 

pipenv run "name of the application"
