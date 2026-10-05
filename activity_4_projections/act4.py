import pygame,math,sys
pygame.init();W,H=900,650;screen=pygame.display.set_mode((W,H));pygame.display.set_caption('Activity 4: 3D Projection Engine');clock=pygame.time.Clock();font=pygame.font.Font(None,28)
V=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)];E=[(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
def rot(p,ax,ay,az):
 x,y,z=p;cx,sx=math.cos(ax),math.sin(ax);y,z=y*cx-z*sx,y*sx+z*cx;cy,sy=math.cos(ay),math.sin(ay);x,z=x*cy+z*sy,-x*sy+z*cy;cz,sz=math.cos(az),math.sin(az);return x*cz-y*sz,x*sz+y*cz,z
def ortho(x,y,z):return int(450+x*150),int(325-y*150)
def oblique(x,y,z,cab):
 a=math.radians(63.4 if cab else 45);L=.5 if cab else 1.;return int(450+(x+z*L*math.cos(a))*150),int(325-(y+z*L*math.sin(a))*150)
def persp(x,y,z,D=4):
 d=max(.1,z+D);return int(450+(x*D/d)*150),int(325-(y*D/d)*150)
mode=0;ax=ay=az=0.;run=True
while run:
 dt=clock.tick(60)/1000
 for ev in pygame.event.get():
  if ev.type==pygame.QUIT:run=False
  if ev.type==pygame.KEYDOWN:
   if ev.key in (pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4):mode=ev.key-pygame.K_1
   if ev.key==pygame.K_ESCAPE:run=False
 k=pygame.key.get_pressed();ax+=(k[pygame.K_DOWN]-k[pygame.K_UP])*1.5*dt;ay+=(k[pygame.K_RIGHT]-k[pygame.K_LEFT])*1.5*dt;az+=(k[pygame.K_e]-k[pygame.K_q])*1.5*dt
 screen.fill((248,248,248));P=[]
 for x,y,z in V:
  x,y,z=rot((x,y,z),ax,ay,az)
  P.append(ortho(x,y,z) if mode==0 else oblique(x,y,z,mode==2) if mode in (1,2) else persp(x,y,z+3))
 for a,b in E:pygame.draw.line(screen,(30,70,120),P[a],P[b],3)
 names=['Orthographic','Cavalier','Cabinet','Perspective'];screen.blit(font.render(f'{names[mode]} | 1-4 projection | Arrows X/Y | Q/E Z',True,(25,25,25)),(20,20));pygame.display.flip()
pygame.quit();sys.exit()
