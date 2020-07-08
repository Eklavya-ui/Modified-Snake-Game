import pygame
from random import randint

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bgsong.mp3")
pygame.mixer.music.play()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,175,0)
blue = (0,0,255)


sc_width = 900
sc_height = 600

bgimg = pygame.image.load("bgpic.png")
bgimg = pygame.transform.scale(bgimg, (sc_width, sc_height))

gameWindow = pygame.display.set_mode((sc_width, sc_height))

pygame.display.set_caption("Snakes")
clock = pygame.time.Clock()

snake_x = randint(50,850)
snake_y = randint(30,575)
snake_size = 5
snake = []
snk_len = 1
i = 1

speed = 2
velocity_x = 0
velocity_y = 0

food_size = 10
food_x = randint(7,892)
food_y = randint(27,593)

fps = 100
score = 0

font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiuibold", 20)

exit_game = False
game_over = False

def plot_snake(snake):
    for x,y in snake:
        pygame.draw.circle(gameWindow,green,[x,y],snake_size)
while not exit_game:
    if game_over:
        gameWindow.fill(white)
        font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiuibold", 50)
        text = font.render("Game Over", True, blue)
        gameWindow.blit(text, [sc_width//2 - 100, sc_height//2 - 30])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
    else:
        gameWindow.blit(bgimg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if velocity_y + speed == 0:
                        velocity_y += (2*speed)
                    else:
                        velocity_y += speed
                    velocity_x = 0
                if event.key == pygame.K_UP:
                    if velocity_y - speed == 0:
                        velocity_y -= (2*speed)
                    else:
                        velocity_y -= speed
                    velocity_x = 0
                if event.key == pygame.K_LEFT:
                    if velocity_x - speed == 0:
                        velocity_x -= (2*speed)
                    else:
                        velocity_x -= speed
                    velocity_y = 0
                if event.key == pygame.K_RIGHT:
                    if velocity_x + speed == 0:
                        velocity_x += (2*speed)
                    else:
                        velocity_x += speed
                    velocity_y = 0

                if snake_x <= 5 or snake_y <= 25 or snake_x >= 895 or snake_y >= 595 :
                    game_over = True
                    print(snake_y, snake_x)

        snake_x += velocity_x
        snake_y += velocity_y

        if score >= 100 * i:
            speed = speed + 1
            i += 1

        if abs(snake_x - food_x) <= 6 and abs(snake_y - food_y) <= 6:
            score += 10
            snk_len += 5
            food_x = randint(10,890)
            food_y = randint(7,593)

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake.append(head)

        if len(snake) > snk_len:
            del snake[0]

        if head in snake[:-1]:
            game_over = True

        gameWindow.fill(white)
        text = font.render(f"Score : {score}", True, blue)
        gameWindow.blit(text, [4,0])
        plot_snake(snake)
        pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])

        pygame.draw.line(gameWindow,black,[5,25],[5,595],2)
        pygame.draw.line(gameWindow,black,[5,25],[895,25],2)
        pygame.draw.line(gameWindow,black,[895,25],[895,595],2)
        pygame.draw.line(gameWindow,black,[5,595],[895,595],2)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
