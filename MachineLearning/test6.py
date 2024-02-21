import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
n,nolable,k = map(int, input().split())  #n: lable, notest: nolable , neighboor k;
data = [] #create table
for i in range(n):
   x,y,lable = map(int, input().split())
   data.append([x,y,lable])
print(data)
test=[]
for i in range(nolable):
    x,y,a = map(int, input().split())
    test.append=([x,y,a])
    


    
