import pygame

class Barrier():
    def __init__(self,screen:pygame.surface.Surface,pos,size_multiplyer:float):
        self.screen = screen
        self.image_states = []
        self.health = 4
        self.pos = pos
        self.alive = True
        self.size = 32*size_multiplyer

        self.hitbox = pygame.Rect(self.pos[0],self.pos[1],self.size,self.size)

        for i in range(3,-1,-1):
            self.image_states.append(pygame.transform.scale(pygame.image.load(f"images/barrier_{i}.png"),(self.size,self.size)))


    def damage(self):
        pass


    def draw(self):
        if self.alive:
            self.screen.blit(self.image_states[self.health-1], self.hitbox)


    def update(self):
        self.damage()
        self.draw()

