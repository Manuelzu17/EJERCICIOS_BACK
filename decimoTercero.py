# You can use the pip freeze command to list all the installed packages
#  and their versions, and then write the output to a file:
import subprocess

with open("dependencies.txt", "w") as f:
    result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
    f.write(result.stdout.decode())

#This will create a file called dependencies.txt 
# that contains the list of installed packages.