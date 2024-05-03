import pygame 
import random
import time

screen_width = 1280
screen_height = 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Particle-Simulation")
pygame.font.init()

WHITE = ((255,255,255))
DARKER_GREY = ((30,30,30))



class Partikel:
     def __init__(self):
          self.size = (9)
          self.gravity = 0.1
          self.x = random.randint(-1,screen_width)
          self.y = random.randint(-1,screen_height)
          self.color = ((255, 255,255))  # Define color as a tuple
          self.speed_x = (0)
          self.speed_y = (random.randint(1,2))
          self.speed_limit = 5
     def move(self): 
          self.speed_y += self.gravity
          
          if self.speed_y > self.speed_limit:
               self.speed_y = self.speed_limit

          self.x += self.speed_x
          self.y += self.speed_y

          if self.x < 0:
               self.x = 0
               self.speed_x *= -1
          elif self.x > screen_width:
               self.x = screen_width
               self.speed_x *= 1
          
          if self.y < 0:
               self.y = 0
               self.speed_y *= -1
          elif self.y > screen_height:
               self.y = screen_height
               self.speed_y *= -1
               
          
          
     def draw(self):
          pygame.draw.circle(screen, self.color ,(int(self.x),int(self.y)), self.size,)
          keys = pygame.key.get_pressed()
          if keys[pygame.K_LEFT]:
               self.x -= 2
          elif keys[pygame.K_RIGHT]:
               self.x += 2
          elif keys[pygame.K_ESCAPE]:
               time.sleep(0.01)
               self.x = random.randint(-1,screen_width)
               self.y = random.randint(-1,screen_height)
          elif keys[pygame.K_s]:
               time.sleep(1)

particles = [Partikel() for _ in range(0)]

font = pygame.font.Font(None, 36) 
text = font.render("Random: ESCAPE", True, WHITE)
text_2 = font.render("Time-Freeze: S", True, WHITE)
text_3 = font.render("Move-right: K_RIGHT", True, WHITE)
text_4 = font.render("Move-left: K_LEFT", True, WHITE)
text_5 = font.render("Spawn: LEFT-CLICK", True, WHITE)
run = True
while run:
     screen.fill(DARKER_GREY)
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
          elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                         particles.append(Partikel())

     
     
     for particle in particles:
          particle.move()
          particle.draw()

     
     screen.blit(text, (screen_width // 10 - text.get_width() // 2, screen_height // 5 - text.get_height() // 10))
     screen.blit(text_2, (screen_width // 10 - text.get_width() // 2, screen_height // 4 - text.get_height() // 10))
     screen.blit(text_3, (screen_width // 10  - text.get_width() // 2, screen_height // 3 - text.get_height() // 10))
     screen.blit(text_4, (screen_width // 10 - text.get_width() // 2, screen_height // 2.5 - text.get_height() // 10))
     screen.blit(text_5, (screen_width // 10 - text.get_width() // 2, screen_height // 2 - text.get_height() // 10))  
     pygame.display.flip()




     clock.tick(60)
pygame.quit()





