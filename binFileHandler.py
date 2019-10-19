from PIL import Image


masked = 251
unused = 252
coastlines = 253
landmask = 254
missing = 255

def get_bytes_from_file(filename):
    return open(filename, "rb").read()



fileBytes = get_bytes_from_file("nt_20151216_f17_v1.1_n.bin")
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

print("Scaling Factor: " + scalingFactor)


print("iCoord: " + icoordinate)

print("jCoord: " + jcoordinate)

print("latEnclosed: " + latEnclosed)

print("GreenwichOrient: " + greenwichOrientation)




#print(headerString)

mode = "L"
size = 304 , 448

img = Image.frombytes(mode, size, imgBytes)

img.save("testImage.png")
