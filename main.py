import pygame
import random

pygame.init()

# creating screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SCISSOR-PAPER-ROCK')

# creating text
h_font = pygame.font.SysFont(None, 50)
human_text = h_font.render('HUMAN', True, (0, 200, 0))
c_font = pygame.font.SysFont(None, 50)
computer_text = h_font.render('COMPUTER', True, (0, 200, 0))

# choices
choices = ['scissors', 'paper', 'rock']
human_choices = ' '

# loading instructions
instruction_font = pygame.font.SysFont(None,30)
instruction_text = instruction_font.render('S for scissors   P for paper  R for rock',True,(0,0,200))

# loading images
rock_img = pygame.transform.scale(pygame.image.load('rock.png'), (200, 200))
scissor_img = pygame.transform.scale(pygame.image.load('scissor.png'), (200, 200))
paper_img = pygame.transform.scale(pygame.image.load('paper.png'), (200, 200))

# losing winning
w_font = pygame.font.SysFont(None, 150)
win_text = w_font.render('YOU WON', True, (200, 0, 0))
l_font = pygame.font.SysFont(None, 150)
loss_text = w_font.render('YOU LOSS', True, (200, 0, 0))
d_font = pygame.font.SysFont(None, 150)
draw_text = d_font.render('DRAW', True, (200, 0, 0))


def you_win():
    screen.blit(win_text, (90, 300))


def you_lose():
    screen.blit(loss_text, (90, 300))


def you_draw():
    screen.blit(draw_text, (90, 300))


# loop
running = True
while running:
    screen.fill('white')
    screen.blit(human_text, (50, 100))
    screen.blit(computer_text, (350, 100))
    screen.blit(instruction_text,(10,40))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                human_choices = 'scissors'
                computer_choices = random.choice(choices)

            if event.key == pygame.K_p:
                human_choices = 'paper'
                computer_choices = random.choice(choices)

            if event.key == pygame.K_r:
                human_choices = 'rock'
                computer_choices = random.choice(choices)

    if human_choices == 'scissors' and computer_choices == 'paper':
        screen.blit(scissor_img, (50, 400))
        screen.blit(paper_img, (350, 400))
        you_win()

    if human_choices == 'scissors' and computer_choices == 'rock':
        screen.blit(scissor_img, (50, 400))
        screen.blit(rock_img, (350, 400))
        you_lose()
    if human_choices == 'rock' and computer_choices == 'paper':
        screen.blit(rock_img, (50, 400))
        screen.blit(paper_img, (350, 400))
        you_lose()

    if human_choices == 'rock' and computer_choices == 'scissors':
        screen.blit(rock_img, (50, 400))
        screen.blit(scissor_img, (350, 400))
        you_win()

    if human_choices == 'paper' and computer_choices == 'scissors':
        screen.blit(paper_img, (50, 400))
        screen.blit(scissor_img, (350, 400))
        you_lose()

    if human_choices == 'paper' and computer_choices == 'rock':
        screen.blit(paper_img, (50, 400))
        screen.blit(rock_img, (350, 400))
        you_win()

    if human_choices == 'paper' and computer_choices == 'paper':
        screen.blit(paper_img, (50, 400))
        screen.blit(paper_img, (350, 400))
        you_draw()

    if human_choices == 'rock' and computer_choices == 'rock':
        screen.blit(rock_img, (50, 400))
        screen.blit(rock_img, (350, 400))
        you_draw()

    if human_choices == 'scissors' and computer_choices == 'scissors':
        screen.blit(scissor_img, (50, 400))
        screen.blit(scissor_img, (350, 400))
        you_draw()

    pygame.display.update()
