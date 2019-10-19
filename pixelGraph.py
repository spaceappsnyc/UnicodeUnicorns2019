try:
    import Image
except ImportError:
    from PIL import Image
import numpy



def main(filename):
    input_img = Image.open(filename)

    input_img.convert('RGB')
    data = input_img.load()
    mask = None
    pixels = get_pixels(data, input_img.size)
    print(pixels[0][0])

    #histogram = make_histogram(pixels)
    #print(histogram)
    reddist = get_reddist(pixels)
    print(reddist)



def get_pixels(data, size):
    pixels = []
    for y in range(size[1]):
        pixels.append([])
        for x in range(size[0]):
            pixels[y].append(data[x,y])
    return pixels

def get_reddist(pixels):
    lowred = 84
    midred = 168
    hired = 252
    lowredcount = 0
    midredcount = 0
    hiredcount = 0
    totcount = 0

    for x in pixels:
        for y in x:
            if y[0] > numpy.average(y):
                if y[0] < lowred:
                    lowredcount += 1
                elif y[0] < midred:
                    midredcount += 1
                else:
                    hiredcount += 1
                totcount += 1

    reddist = []
    reddist.append(lowredcount/totcount)
    reddist.append(midredcount/totcount)
    reddist.append(hiredcount/totcount)
    return reddist


def make_histogram(pixels):
    colors = {}
    for x in pixels:
        for y in x:
            colset = []
            for n in y:
                a = numpy.floor(n / 10) * 10
                colset.append(str(a))
            colhash = "#".join(colset)
            if colhash in colors:
                colors[colhash] += 1
            else:
                colors[colhash] = 1
    return colors



if __name__ == "__main__":
    main("./localImage.jpg")