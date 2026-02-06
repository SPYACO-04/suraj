import os
#specify the dictory you want to list
directory_path = '/documents'

#list all files and directories in the specified path
contents =os.listdir(directory_path)

#print each file and directory name
for item in contents:
    print(item)