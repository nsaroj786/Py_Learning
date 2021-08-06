#!usr/bin/python

print ("### File I/O ###")

file = open('file_io.txt')		#opens the file and saves the data into variable
print(file)
print(file.read())				#read the data
print(file.read())				#once rade, it does not repeat
print(file.read())
print(file.read())

file.seek(0)					#moves to start again, can be run again
print(file.read())				
file.seek(0)
print(file.read())
file.seek(0)
print(file.read())

file.seek(0)					#Move cursor to start of file
print("### Read Line###")
print (file.readline())			#Reads one line from start of the file
print (file.readline())
print (file.readline())

file.seek(0)
print("### Read Lines###")
print (file.readlines())

file.close()

## Another way to open and close a file
print("Another way to handale files")
with open('file_io.txt', mode='r+') as my_file:	# r+ -> read and write
	print(my_file.readlines())
	##no need to close, automatically will close
	text = my_file.write('Hey, its me !!')
	print(text)

'''try:
	with open('file_io.txt', mode='r+') as my_file:	# r+ -> read and write
	print(my_file.readlines())
except FileNotFoundError as err:
	print("file does not exist.")
	raise err '''
	
	
	
	
