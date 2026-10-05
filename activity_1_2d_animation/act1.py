import pygame, math, sys
pygame.init()
W,H=800,600; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption('Activity 1: 2D Animation'); clock=pygame.time.Clock(); font=pygame.font.Font(None,28)
def lerp(a,b,t): return a+(b-a)*t
def lerp_point(a,b,t): return (lerp(a[0],b[0],t),lerp(a[1],b[1],t))
def path_pos(points,duration,elapsed):
    u=(elapsed%duration)/duration; s=u*(len(points)-1); i=min(int(s),len(points)-2); t=s-i; t=t*t*(3-2*t); return lerp_point(points[i],points[i+1],t)
tri=[(300,230),(390,230),(345,360),(345,360)]; rect=[(280,220),(430,220),(430,370),(280,370)]
path=[(100,120),(250,100),(420,180),(600,120),(700,300)]; elapsed=0; mode=1
bx,by,bvx,bvy=150.,100.,180.,0.; g=900.; e=.75; floor=520; r=25
run=True
while run:
    dt=clock.tick(60)/1000; elapsed+=dt
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: run=False
        if ev.type==pygame.KEYDOWN:
            if ev.key in (pygame.K_1,pygame.K_2,pygame.K_3): mode=ev.key-pygame.K_0
            if ev.key==pygame.K_ESCAPE: run=False
    screen.fill((245,245,245))
    if mode==1:
        pygame.draw.lines(screen,(180,180,180),False,path,2); p=path_pos(path,5,elapsed); pygame.draw.circle(screen,(60,120,230),(int(p[0]),int(p[1])),24); title='1 - Tweening / LERP'
    elif mode==2:
        t=(math.sin(elapsed*1.2)+1)/2; p=[lerp_point(a,b,t) for a,b in zip(tri,rect)]; pygame.draw.polygon(screen,(80,190,255),p); pygame.draw.polygon(screen,(20,50,80),p,3); title='2 - Polygon Morphing'
    else:
        bx+=bvx*dt; bvy+=g*dt; by+=bvy*dt
        if by+r>=floor: by=floor-r; bvy=-abs(bvy)*e
        if bx-r<=0: bx=r; bvx=abs(bvx)
        if bx+r>=W: bx=W-r; bvx=-abs(bvx)
        pygame.draw.line(screen,(70,70,70),(0,floor),(W,floor),3); pygame.draw.circle(screen,(235,80,80),(int(bx),int(by)),r); title='3 - Bouncing Dynamics'
    screen.blit(font.render(f'{title} | Press 1, 2, or 3',True,(30,30,30)),(20,20)); pygame.display.flip()
pygame.quit(); sys.exit()
