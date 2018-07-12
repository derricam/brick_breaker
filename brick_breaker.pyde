xCoord = random(0, 200) 
yCoord = random (100, 500) 

xSpeed = 6
ySpeed = 6
ellipseSize = 40
def setup(): 
    size(800, 600) 
    background("#502E20")
def draw(): 
    background("#502E20") 
    global xCoord, yCoord,y, xSpeed, ySpeed, ellipseSize 
    leftBoundary = ellipseSize / 2 
    rightBoundary = 800 - ellipseSize / 2 
    topBoundary = ellipseSize / 2  
    ybrickBoundary = 125 - ellipseSize / 2  
    xbrickBoundary = ellipseSize / 2
    bottomBoundary = 600 - ellipseSize /2 
    xCoord += xSpeed 
    yCoord += ySpeed 
    if xCoord >= rightBoundary or xCoord<= leftBoundary: 
        xSpeed = -xSpeed  
    if yCoord >= bottomBoundary or yCoord<= topBoundary: 
        ySpeed = -ySpeed   
    
    fill(255, 255, 255) 
    ellipse(xCoord, yCoord, ellipseSize, ellipseSize) 
    #fill(random (255),random(255),random(255))
    rect(0,0,100,80) 
    rect(100,0,100,80)
    rect(200,0,100,80)
    rect(300,0,100,80)
    rect(400,0,100,80)
    rect(500,0,100,80)
    rect(600,0,100,80)
    rect(700,0,100,80) 

        
    
    
    
    
    
    
