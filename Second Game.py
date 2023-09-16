import pygame
from sys import exit
from random import randint

def display_score():
    time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'{time}', False, (0, 0, 0))
    score_rect = score_surface.get_rect(center = (500, 200))
    screen.blit(score_surface, score_rect)

def move_obstacle(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            screen.blit(spike, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return[]

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("loco")
clock = pygame.time.Clock()

player = pygame.image.load('C:\\Users\\Robert\\Downloads\\Player2.png')
ground = pygame.image.load('C:\\Users\\Robert\\Downloads\\Ground1.png')
sky = pygame.image.load('C:\\Users\\Robert\\Downloads\\Sky1.png')
replay = pygame.image.load('C:\\Users\\Robert\\Downloads\\Replay.png')
replay2 = pygame.image.load('C:\\Users\\Robert\\Downloads\\Replay2.png')
font = pygame.font.Font(None, 40)
#text_surface = text.render('Score', True, (89, 89, 89))
gameover = font.render('GAME OVER', True, 'White')

spike = pygame.image.load('C:\\Users\\Robert\\Downloads\\Spike1.png').convert_alpha()
nuke = pygame.image.load('C:\\Users\\Robert\\Downloads\\Nuke.png')
nuke_rect = nuke.get_rect(midbottom = (50, 430))
spikebox = pygame.draw.rect(screen, 'Pink', pygame.Rect(30, 30, 40, 50))
spike_rect = spike.get_rect(midbottom = (500, 550)) 
obstacle_list = []

border = (50, 492)
player_rect = player.get_rect(midbottom = (50, 550))
       
text_rect = gameover.get_rect(midbottom = (500, 45))
replay_rect = replay.get_rect(center = (500, 300))

replay2_rect = replay2.get_rect(center = (500, 300))
gravity = 0
running = True

start_time = 0
spike_timer = pygame.USEREVENT + 1
pygame.time.set_timer(spike_timer,1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom >= 550:
                    gravity = -20
        
        if event.type == spike_timer and running:
            obstacle_list.append(spike.get_rect(midbottom = (randint(700, 1000), 550)))

        
    
    
    
    if running:

        
        
        screen.blit(sky,(0, 0))
        display_score() 
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 550:
            player_rect.bottom = 550
        screen.blit(player,player_rect)

        obstacle_list = move_obstacle(obstacle_list)

        
        
        
        
    

        screen.blit(ground,(0,550))
        #screen.blit(text_surface, text_rect)
        #spike_rect.x -= 6
        #if spike_rect.right <= 0:
            #spike_rect.left = 1000
            
        screen.blit(spike,spike_rect)
        screen.blit(nuke, nuke_rect)
        
        
        #pygame.draw.line(screen,'Pink', (0, 0), pygame.mouse.get_pos(), 10)

        if player_rect.colliderect(spike_rect):
            running = False
    else:
        screen.fill('#2e2e2e')
        #screen.blit(gameover, text_rect)
        screen.blit(replay, replay_rect)
        screen.blit(gameover,text_rect)
        if replay_rect.collidepoint(mousepos):
            screen.blit(replay2, replay2_rect)
    
        
    
        
        #pygame.draw.rect(screen, 'Pink', replay_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if replay_rect.collidepoint(mousepos):
                running = True
                spike_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
    

        
                

            
    


    mousepos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mousepos):
        #print('true')

    
    pygame.display.update()
    clock.tick(60) 