import os
# printd current working directory
# print(os.getcwd())

# # os.chdir('C:\Users\User\OneDrive - Lord Buddha Education Foundation\Desktop   ')

# print(os.listdir())

# os.mkdir('Os-Demo')




# os.makedirs('test.py')

print(os.listdir())

for dirpath, dirnames, filenames in os.walk ("c:/Users/User/OneDrive - Lord Buddha Education Foundation/Desktop/Python"):
  print('Current Path', dirpath)
  print("Dir name",dirnames)
  print('File Name', filenames)