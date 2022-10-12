class Solution(object):
    def flipAndInvertImage(self, image):
        newImage = []
        for x in range(0,len(image)):
            image[x].reverse()
        print(image)
        for x in range(0,len(image)):
            for y in range(0,len(image[x])):
                if image[x][y] == 0:
                    image[x][y] = 1
                else:
                    image[x][y] = 0
        return image
