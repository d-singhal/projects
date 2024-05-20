import pickle

# Pickling is used for storing data in binary format. Just like the pickle which is stored for a long time and is accessible when
# whenever in use. 
'''Pickling:
Pickling is the name of the serialization process in Python. Any object in Python can be serialized into a byte stream and dumped as a file in the memory. The process of pickling is compact but pickle objects can be compressed further. Moreover, pickle keeps track of the objects it has serialized and the serialization is portable across versions.
The function used for the above process is pickle.dump().

Unpickling:
Unpickling is the complete inverse of pickling. It deserializes the byte stream to recreate the objects stored in the file and loads the object to memory.
The function used for the above process is pickle.load().'''

names = ['divya', 'anil','sharul']

fileobj =  open('myfile.pkl', 'wb')
pickle.dump(names, fileobj)
fileobj.close

fileobj = open('myfile.pkl', 'rb')
cars =  pickle.load(fileobj)
print(cars)