def rojo(img2, img):
    matriz = img2
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if i == 0 and j == 0: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1):
                    matriz[i][j] = (255,0,0)

            elif i == len(img) and j == len(img[i]) - 1: 
                if img[i][j] == 0 and (img[i][j-1] == 1 or img[i-1][j] == 1):
                    matriz[i][j] = (255,0,0)

            elif i == 0 and j > 0 and j < len(img[i]) - 1: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1 or img[i][j-1] == 1):
                    matriz[i][j] = (255,0,0)

            elif j == 0 and i > 0 and i < len(img) - 1: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1 or img[i-1][j] == 1):
                    matriz[i][j] = (255,0,0)

            elif i > 0 and i < len(img) - 1 and j > 0 and j < len(img[i]) - 1: 
                if img[i][j] == 0 and (img[i][j+1] == 1 or img[i+1][j] == 1 or img[i-1][j] == 1 or img[i][j-1] == 1):
                    matriz[i][j] = (255,0,0)

    return matriz

