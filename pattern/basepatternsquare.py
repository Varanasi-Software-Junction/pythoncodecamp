#the figure to be drawn
# https://github.com/Varanasi-Software-Junction/pythoncodecamp/blob/ba8654ec5f4118ca6d366c4dbc478886b4c1288e/pattern/patterns/square.PNG

n = 7 #n=no of rows and no of columns as well
for row in range(1, n + 1): # loop for rows
    for col in range(1, n + 1):# loop for columns
        print("0", end="") # print 0 end = "" is for avoiding the newline
    print() # print newline after col loop finishes

