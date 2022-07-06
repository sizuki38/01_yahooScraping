import pickle, sys

with open(sys.argv[1],'rb')as f:
    data = pickle.load(f)
    data.replace('\n','')
print(data)