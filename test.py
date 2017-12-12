import numpy as np
import time
import json
import codecs
import random

data = {}
# data['people'] = []
# data['people'].append(
#     {
#         'name': 'Scott',
#         'website': 'abc.com',
#         'from' : 'Web'
#     }
# )
#
# data['people'].append(
#     {
#         'name': 'Larry',
#         'website': 'def.com',
#         'from' : 'Mi'
#     }
# )
#
# data['people'].append(
#     {
#         'name': 'Tim',
#         'website': 'fds.com',
#         'from' : 'Al'
#     }
# )
# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)
#     print("OK")
#
data['matrix'] = []
A = np.array(
    [[1,2],
    [3,4],
    [5,6]]
)
B = np.array(
    [[5,2],
    [3,0],
    [5,7]]
)
data['matrix'].append(A)
# data['matrix'].append(B)
# print(data['matrix'])
# print('start')
# with open('data.txt', 'w', encoding='utf-8') as outfile:
#     json.dump(data, outfile)
#     print("OK")

data2 = [[[0]*2]*3]*2
mask = np.array([
    [2,3,2],
    [3,3,3]
])
data4 = np.random.randint(3,size=(512,512))
data3 = np.random.randint(1,size=(512,512,10))
data5 = np.random.randint(1,size=(512,512,10))
startTime = time.time()
for i in range(10):
    data3[:,:, i] = np.where(
        data4 == 2,
        data3[:,:,i] + 1,
        data3[:,:, i]
    )
print("time: ", time.time() - startTime)
# print(data3)
startTime = time.time()
for i in range(10):
    for j in range(512):
        for k in range(512):
            if data4[j][k] == 2:
                data5[j][k][i] = 1
print("time: ", time.time() - startTime)
for i in range(10):
    for j in range(512):
        for k in range(512):
            if data3[j][k][i] != data5[j][k][i]:
                print("Wrong")
print("OK")


from skimage.io import imread_collection

#your path 
col_dir = 'cats/*.jpg'

#creating a collection with the available images
col = imread_collection(col_dir)