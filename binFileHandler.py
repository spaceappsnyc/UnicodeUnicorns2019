from PIL import Image
import pandas as pd
import numpy


masked = 251
unused = 252
coastlines = 253
landmask = 254
missing = 255

def get_bytes_from_file(filename):
    return open(filename, "rb").read()

def div_by_250(x):
    return x/250

def get_col_row_from_lat_long(i,j,lat, long):
    col = j + 150 * (90-lat)/(90-56.35) * numpy.cos(long - 45)
    row = i - 234 * (90-lat)/(90-39.43) * numpy.cos(long - 45)
    return (col, row)


fileBytes = get_bytes_from_file("dataset/nt_20151216_f17_v1.1_n.bin")
headerBytes = fileBytes[0:299]
imgBytes = fileBytes[300:]

headerString = headerBytes.decode("ascii")

missingData = headerBytes[0:5].decode('ascii')
columnsInPolarGrid = headerBytes[6:11].decode('ascii')
rowsInPolarGrid = headerBytes[12:17].decode('ascii')
bullshit = headerBytes[18:23].decode('ascii')
latEnclosed = headerBytes[24:29].decode('ascii')
greenwichOrientation = headerBytes[30:35].decode('ascii')
moreBullshit = headerBytes[36:41].decode('ascii')
jcoordinate = headerBytes[42:47].decode('ascii')
icoordinate = headerBytes[48:53].decode('ascii')
scalingFactor = headerBytes[120:125].decode('ascii')

print(headerString)
"""
print("Scaling Factor: " + scalingFactor)


print("iCoord: " + icoordinate)

print("jCoord: " + jcoordinate)

print("latEnclosed: " + latEnclosed)

print("GreenwichOrient: " + greenwichOrientation)
"""

#ser = ser.replace(masked, numpy.NaN)
#ser = ser.replace(unused, numpy.NaN)
#ser = ser.replace(coastlines, numpy.NaN)
#ser = ser.replace(landmask, numpy.NaN)
#ser = ser.replace(missing, numpy.NaN)
#map(div_by_250, ser)

#print(ser[0])

#print(numpy.mean(ser))
#print(numpy.count_nonzero(ser[ser > ser.median()]))
#print(numpy.count_nonzero(ser))


#print(headerString)


mode = "L"
size = 304 , 448

retx = 170
rety = 249


intArray = [x for x in imgBytes]
tupleArray = []


for i in range(304*448):
    if intArray[i - 1] == masked:
        tupleArray.append((255,255,0))
    elif intArray[i - 1] == unused:
        tupleArray.append((255,0,0))
    elif intArray[i - 1] == coastlines:
        tupleArray.append((0,128,128))
    elif intArray[i - 1] == landmask:
        tupleArray.append((0,255,0))
    elif intArray[i - 1] == missing:
        tupleArray.append((255,255,255))
    else:
        tupleArray.append((0,0,intArray[i - 1]))


"""
for i in range(304 * 448):
    if i % 304 == retx and i // 304 == rety:
        print("The value is " + str(intArray[i]/250))
    elif i == retx:
        intArray[i] = 0
    elif i % 304 == retx:
        intArray[i] = 0
    elif i // 304  == rety:
        intArray[i] = 0


imgBytes = bytes(intArray)
"""
"""
0123  1234
4567  5678
89ab  9abc
"""
img = Image.frombytes(mode, size, imgBytes)



img.save("testImage.png")


