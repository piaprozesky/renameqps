# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 

folder = "."

for count, filename in enumerate(os.listdir(folder)): 

    source = filename
    sourceLower = filename.lower()
    if("memo" in sourceLower):
    	dst =  'modified'
    	print(sourceLower)
    	# rename all files
    	# os.rename(source, dest)