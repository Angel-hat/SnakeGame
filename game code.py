
import pygame,random
pygame.init()
pygame.display.set_caption("Tanisha game")

W,H=1200,600
w,h=50,50

screen=pygame.display.set_mode([W,H])    

black=0,0,0

audio=pygame.mixer.Sound("sound.wav")
red=255,0,0
blue=0,0,255


def gameOver():
    font1=pygame.font.SysFont(None,50)
    font1=font1.render(f"GameOver\nPress space to restart",True,red)
    
    while True:
        for event in pygame.event.get():  #controls
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game()
        screen.blit(font1,(50,50))
        pygame.display.update()

def score(count):
    font=pygame.font.SysFont(None,50)
    font=font.render(f"Score:{count}",True,blue)
    screen.blit(font,(W-200,50))
    
def DrawSnake(snakeList):
    for i in snakeList:
        pygame.draw.rect(screen,black,(i[0],i[1],50,50))
        
def game():
    i=0
    j=0
    mx=0
    my=0
    
    green=0,255,0
    white=255,255,255
    snakeLength=1
    snakeList=[]#storing coordinates
    count=0
    dora_w,dora_h=50,50
    dora_x,dora_y=random.randint(0,W-dora_w),random.randint(0,H-dora_h)
    dora=pygame.image.load("doracake.jpg")
    dora=pygame.transform.scale(dora,(dora_w,dora_h))
    
    
    while True:
        for event in pygame.event.get():  #controls
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    mx=0
                    my=-1
                elif event.key==pygame.K_DOWN:
                    mx=0
                    my=1
                elif event.key==pygame.K_LEFT:
                    mx=-1
                    my=0
                elif event.key==pygame.K_RIGHT:
                    mx=1
                    my=0
        i+=mx
        j+=my
        if i<0:
            i=W-w
        elif i>W-w:
            i=0
        elif j>H-h:
            j=0
        elif j<0:
            j=H-h
        screen.fill(green)
        snake=pygame.draw.rect(screen,red,[i,j,w,h])#now behaving like imagenary rect
            
        food=pygame.Rect((dora_x,dora_y,dora_w,dora_h))
        screen.blit(dora,(dora_x,dora_y))

        snakeHead=(i,j)
        snakeList.append(snakeHead)
        DrawSnake(snakeList)
        score(count)
        
        if len(snakeList)>snakeLength:#if coordinates in snakeList>snakelength(1,10 etc)
            del snakeList[0]
            
        if snakeList[-1] in snakeList[:-1]:
            gameOver()
        if snake.colliderect(food):
            dora_x,dora_y=random.randint(0,W-dora_w),random.randint(0,H-dora_h)
            audio.play(0)
            count+=1
            snakeLength+=10 #responsible for increase in length of snake after collison

        pygame.display.update() #pygame.display.flip()
game()
    #To import music and sounds
        #1 download from chrome(either mp3 or .wav
        #2 audio=pygame.mixer.Sound("file name,extension")
        #3 audio.play(0)
