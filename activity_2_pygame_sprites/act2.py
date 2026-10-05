import pygame,random,sys
pygame.init(); W,H=800,600; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption('Activity 2: Sprite Collision Arena'); clock=pygame.time.Clock(); font=pygame.font.Font(None,32)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(); self.image=pygame.Surface((42,42),pygame.SRCALPHA); pygame.draw.circle(self.image,(44,94,138),(21,21),21); self.rect=self.image.get_rect(center=(W//2,H//2)); self.speed=5
    def update(self):
        k=pygame.key.get_pressed(); self.rect.x+=(k[pygame.K_RIGHT]-k[pygame.K_LEFT])*self.speed; self.rect.y+=(k[pygame.K_DOWN]-k[pygame.K_UP])*self.speed; self.rect.clamp_ip(screen.get_rect())
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(); s=random.randint(28,45); self.image=pygame.Surface((s,s),pygame.SRCALPHA); pygame.draw.rect(self.image,(220,60,70),self.image.get_rect(),border_radius=7); self.rect=self.image.get_rect(center=(random.randint(40,W-40),random.randint(40,H-40))); self.vx=random.choice([-1,1])*random.randint(2,4); self.vy=random.choice([-1,1])*random.randint(2,4)
    def update(self):
        self.rect.x+=self.vx; self.rect.y+=self.vy
        if self.rect.left<=0 or self.rect.right>=W:self.vx*=-1
        if self.rect.top<=0 or self.rect.bottom>=H:self.vy*=-1
        self.rect.clamp_ip(screen.get_rect())
class Particle:
    def __init__(self,pos): self.x,self.y=map(float,pos); self.vx=random.uniform(-3,3); self.vy=random.uniform(-3,3); self.life=255
    def update(self): self.x+=self.vx; self.y+=self.vy; self.life-=10
    def draw(self,s):
        if self.life>0:
            q=pygame.Surface((10,10),pygame.SRCALPHA); pygame.draw.circle(q,(255,220,60,self.life),(5,5),5); s.blit(q,(int(self.x-5),int(self.y-5)))
player=Player(); obstacles=pygame.sprite.Group(Obstacle() for _ in range(7)); group=pygame.sprite.Group(player); particles=[]; score=0; health=100; run=True
while run:
    clock.tick(60)
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: run=False
        if ev.type==pygame.KEYDOWN and ev.key==pygame.K_ESCAPE: run=False
    group.update(); obstacles.update()
    for ob in pygame.sprite.spritecollide(player,obstacles,False):
        score+=1; health=max(0,health-5); particles += [Particle(ob.rect.center) for _ in range(8)]; ob.rect.center=(random.randint(40,W-40),random.randint(40,H-40))
    for p in particles[:]: p.update(); particles.remove(p) if p.life<=0 else None
    screen.fill((235,238,242)); obstacles.draw(screen); group.draw(screen)
    for p in particles:p.draw(screen)
    screen.blit(font.render(f'Score: {score}   Health: {health}   FPS: {clock.get_fps():.0f}',True,(25,25,25)),(15,15)); pygame.display.flip()
pygame.quit();sys.exit()
