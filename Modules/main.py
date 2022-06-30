import os
import shutil

path = '/users/alexa/OneDrive/Desktop/os'
print("Before copying the file:")
print(os.listdir(path))
source = "/users/alexa/OneDrive/Desktop/os/source1.txt"
destination = "/users/alexa/OneDrive/Desktop/os/destination.txt"
dest = shutil.copy(source, destination)
print("After copying file: ")
print(os.listdir(path))