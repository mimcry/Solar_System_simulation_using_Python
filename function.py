# lets make multiple tree with the help of function
picture = [[0,0,0,1,0,0,0],
           [0,0,1,1,1,0,0],
           [0,1,1,1,1,1,0],
           [1,1,1,1,1,1,1],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0],]
def salon():
 for row in picture:
    for pixels in row:
     if (pixels==1):
      print("*", end="")          
     else:
      print(" ", end="")
    print("")
salon()
salon()
salon() 