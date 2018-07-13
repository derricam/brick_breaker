xCoord = (640) 
yCoord = (560) 
xSpeed = 6
ySpeed = 6
ellipseSize = 40 
brokenBrick1 = False 
brokenBrick2 = False 
brokenBrick3 = False
brokenBrick4 = False 
brokenBrick5 = False
brokenBrick8 = False 

def setup(): 
    size(800, 600) 
    background("#502E20")
def draw(): 
    background("#502E20") 
    fill("#645C5C")
    paddle = rect(mouseX, 550, 150, 30)
    global xCoord, yCoord,y, xSpeed, ySpeed, ellipseSize, brokenBrick1, brokenBrick2, brokenBrick3, brokenBrick4, brokenBrick5, brokenBrick8 
    leftBoundary = ellipseSize / 2 
    rightBoundary = 800 - ellipseSize / 2 
    topBoundary = ellipseSize / 2  
    ybrickBoundary = 125 - ellipseSize / 2  
    xbrickBoundary = ellipseSize / 2
    bottomBoundary = 600 - ellipseSize /2 
    xCoord += xSpeed 
    yCoord += ySpeed 
    bBrick1 = (xCoord<= 100 and yCoord<=125)
    bBrick8 = (yCoord<=125 and xCoord>=700)  
    bBrick2 = (xCoord<= 199 and xCoord> 100 and yCoord<=125) 
    bBrick3 = (xCoord <= 299 and xCoord >= 200 and yCoord <= 125)
    bBrick4 = (xCoord <= 399 and xCoord >= 300 and yCoord <= 125) 
    bBrick5 = (xCoord<= 499 and xCoord >=400 and yCoord <= 125)
    if xCoord >= rightBoundary or xCoord<= leftBoundary: 
        xSpeed = -xSpeed  
    if yCoord >= bottomBoundary or yCoord<= topBoundary: 
        ySpeed = -ySpeed   
    if yCoord <= ybrickBoundary: 
        ySpeed = -ySpeed  
    
    fill(255, 255, 255) 
    ellipse(xCoord, yCoord, ellipseSize, ellipseSize) 
    #fill(random (255),random(255),random(255)) 
    if(brokenBrick1):
        fill("#502E20") 
    rect(0,0,100,80) 
    
    fill(255, 255, 255) 
    if(brokenBrick2): 
        fill("#502E20")
    rect(100,0,100,80) 
    fill(255, 255, 255) 
    if(brokenBrick3): 
        fill("#502E20") 
    rect(200,0,100,80)  
    if(brokenBrick4): 
        fill("#502E20")
    fill(255, 255, 255) 
    if(brokenBrick5): 
        fill("#502E20")
    rect(300,0,100,80)  
    fill(255, 255, 255)
    rect(400,0,100,80) 
    fill(255, 255, 255)
    rect(500,0,100,80) 
    fill(255, 255, 255)

    rect(600,0,100,80)
    if(brokenBrick8): 
        fill("#502E20") 
    rect(700,0,100,80)  
    if bBrick2: 
        fill("#502E20") 
        brokenBrick2 = True 
        
    if bBrick1:
        fill("#502E20") 
        rect(0, 0, 100, 80) 
        brokenBrick1 = True 
    if bBrick3: 
        fill("#502E20") 
        rect(300, 0, 100, 80) 
        brokenBrick3 = True 
    if bBrick4: 
        fill("#502E20") 
        rect(400, 0, 100, 80) 
        brokenBrick4 = True 
    if bBrick5: 
        fill("#502E20") 
        rect(500, 0, 100, 80) 
        
       

    if bBrick8:
        fill("#502E20") 
        rect(700, 0, 100, 80) 
        brokenBrick8 = True 
        
    
