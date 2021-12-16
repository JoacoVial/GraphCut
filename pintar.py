def rojo(img):
    matriz = [ [ (0,0,0) for i in range(len(img)) ] for j in range(len(img)) ]
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            if i == 0 and j == 0: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1):
                    matriz[i][j] = (255,0,0)

            elif i == len(img) and j == len(img) - 1: 
                if img[i][j] == 0 and (img[i][j-1] == 1 or img[i-1][j] == 1):
                    matriz[i][j] = (255,0,0)

            elif i == 0 and j > 0 and j < len(img) - 1: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1 or img[i][j-1] == 1):
                    matriz[i][j] = (255,0,0)

            elif j == 0 and i > 0 and i < len(img) - 1: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1 or img[i-1][j] == 1):
                    matriz[i][j] = (255,0,0)

            elif i > 0 and i < len(img) - 1 and j > 0 and j < len(img) - 1: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1 or img[i-1][j] == 1 or img[i][j-1] == 1):
                    matriz[i][j] = (255,0,0)

    return matriz

