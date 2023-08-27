import pygame,sys,random,time
t = None
firstchoice = None
k = None
Row = None
Col = None
clicknum = 0
winsize = (1920,990)
w = 212
h = 210
dist = 25
rownum = 4
colnum = 8
indiceslist = []
blitlist =[]
score = 0
GREEN = (0, 255, 0)
BLUE = (0,0,255)
FPS = 60
F_count = 0
Bcase = pygame.transform.smoothscale(pygame.image.load('Briefcase.png'),(w,h))
CD = pygame.transform.smoothscale(pygame.image.load('CD.png'),(w,h))
Barhain = pygame.transform.smoothscale(pygame.image.load('Brhain.png'),(w,h))
Indo = pygame.transform.smoothscale(pygame.image.load('Indo.png'),(w,h))
Ivry = pygame.transform.smoothscale(pygame.image.load('IvryC.png'),(w,h))
Kuwait = pygame.transform.smoothscale(pygame.image.load('Kuwait.png'),(w,h))
Ireland = pygame.transform.smoothscale(pygame.image.load('Ireland.png'),(w,h))
Jordan = pygame.transform.smoothscale(pygame.image.load('JORDAN.png'),(w,h))
Italy = pygame.transform.smoothscale(pygame.image.load('Italy.png'),(w,h))
Quatar = pygame.transform.smoothscale(pygame.image.load('Quatar.png'),(w,h))
Rbin = pygame.transform.scale(pygame.image.load('RecycleBin.png'),(w,h))
Romania = pygame.transform.smoothscale(pygame.image.load('Romania.png'),(w,h))
Chad = pygame.transform.smoothscale(pygame.image.load('Chad.png'),(w,h))
Palestine = pygame.transform.smoothscale(pygame.image.load('Palestine.png'),(w,h))
Monaco = pygame.transform.smoothscale(pygame.image.load('Monaco.png'),(w,h))
Sing = pygame.transform.smoothscale(pygame.image.load('Sing.png'),(w,h))
pic_list = [Bcase,CD,Barhain,Indo,Ivry,Kuwait,Ireland,Jordan,Italy,Rbin,Romania,Chad,Monaco,Sing,Quatar,Palestine]
q = list(range((rownum*colnum)//2))
for row in range(rownum):
    indiceslist.append([])
    blitlist.append([])
    for col in range(colnum):
        indiceslist[row].append(random.choice(q))
        blitlist[row].append(0)
        for i in q:
            if sum([row.count(i) for row in indiceslist]) == 2:
                q.remove(i)
clock = pygame.time.Clock()
running = True
pygame.init()
screen = pygame.display.set_mode(winsize)
while running:
    for rows in range(rownum):
        for column in range(colnum):
            pygame.draw.rect(screen,
                            (255,255,204),
                            ((w+dist)*column+dist,(h+dist)*rows+dist,w,h))
            if blitlist[rows][column] == 1:
                screen.blit(pic_list[indiceslist[rows][column]],((w+dist)*column+dist,(h+dist)*rows+dist))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            Col = pos[0]//(w+dist)
            Row = pos[1]//(h+dist)
            if 0<= Row < len(indiceslist):
                if 0 <= Col < len(indiceslist[Row]):
                    if blitlist[Row][Col] == 0:
                        clicknum +=1
                        if clicknum % 2 == 1:
                            k = ((Row,Col))
                            firstchoice = pic_list[indiceslist[Row][Col]]
                            blitlist[Row][Col] = 1
                        if clicknum % 2 == 0:
                            t = pic_list[indiceslist[Row][Col]]
                            blitlist[Row][Col] = 1
                            if t == firstchoice:
                                score+=1
                            else:
                                screen.blit(pic_list[indiceslist[Row][Col]],((w+dist)*Col+dist,(h+dist)*Row+dist))
                                pygame.display.update()
                                time.sleep(0.5)
                                blitlist[Row][Col] = 0
                                blitlist[k[0]][k[1]] = 0
    if score == colnum*rownum//2:
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render('U win', True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (winsize[0]/2,winsize[1]/2)
        screen.blit(text,textRect)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
random.shuffle(pic_list)
    
    
