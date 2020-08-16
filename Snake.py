import pygame, sys, time, random

pygame.init()
screen_width = 1350
screen_height = 710
clock = pygame.time.Clock()
screen1 = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Times New Roman", 48)
screen2 = pygame.display.set_mode((screen_width, screen_height))

def snake_mov(snake_list):
    for a in snake_list:
        pygame.draw.rect(screen2, (0, 0, 0), [a[0], a[1], 20, 20])


def game():
    global screen_width, screen_height, font

    def game_over():
        nonlocal gameover
        gameover = True
        gameovertext = font.render("GAME OVER", True, (255, 0, 0))
        screen2.blit(gameovertext, (screen_width / 2 - 130, 180))
        play_again_text = font.render("Do you want to play again? ", True, (255, 0, 0))
        screen2.blit(play_again_text, (screen_width/4 + 115 , 330))
        yes_no = font.render("Press Y for YES and N for NO.", True , (255, 0, 0))
        screen2.blit(yes_no, (screen_width/4 + 110 , 430))
        pygame.display.flip()

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_y:
                        game()
                    if e.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()

    fruit_x = random.randint(10, 1300)
    fruit_y = random.randint(10, 660)
    x1 = screen_width/2
    y1 = screen_height/2
    x1_change = 0
    y1_change = 0
    length_of_snake = 1
    snake_List = []
    your_score = 0
    gameover = False


    while not gameover:
        screen2.fill((0, 26, 51))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    y1_change = -2
                    x1_change = 0
                if ev.key == pygame.K_DOWN:
                    y1_change = 2
                    x1_change = 0
                if ev.key == pygame.K_LEFT:
                    x1_change = -2
                    y1_change = 0
                if ev.key == pygame.K_RIGHT:
                    x1_change = 2
                    y1_change = 0


        #If game is over.
        if x1 <= 0 or x1 >= screen_width or y1 <= 0 or y1 >= screen_height:
            game_over()

        fruit = pygame.Rect(fruit_x, fruit_y, 10, 10)

        x1 += x1_change
        y1 += y1_change
        snake = pygame.Rect(x1 , y1 , 20, 20)
        pygame.draw.rect(screen2, (255, 23, 0), fruit)
        snake_head = [x1, y1]
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                gameover = True

        snake_mov(snake_List)


        score = font.render("YOUR SCORE: {}".format(your_score), False, (39, 255, 0))
        screen2.blit(score, (10, 10))
        pygame.display.update()
        clock.tick(100)

        if snake.colliderect(fruit):
            fruit_x = random.randint(10, 1340)
            fruit_y = random.randint(10, 700)
            length_of_snake += 20
            your_score += 1


mouse = pygame.mouse.get_pos()
while True:
    screen1.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            game()
            pygame.quit()
            sys.exit()


    option1 = font.render("To play press any key", False, (0, 255, 0))
    screen1.blit(option1, (screen_width/2-200, screen_height/2-50))

    pygame.display.flip()
