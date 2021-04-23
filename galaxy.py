import pygame,os, random, math
pygame.font.init()

pygame.init()

#game window
width = 900
height = 750
gameWindow = pygame.display.set_mode((width,height))        # for game window
pygame.display.set_caption("Galaxy Wars") 					#for game window title
logo = pygame.image.load("images/f_ball.gif")
pygame.display.set_icon(logo) 								#for game window title

exit_game = False
game_over = False
fps = 60
Score = 0
lives = 5
main_font = pygame.font.SysFont("comicsans", 50)

#background
background_image = pygame.transform.scale(pygame.image.load(os.path.join("images/galaxy.jpg")), (width, height))

#rocket
rocket = pygame.transform.scale(pygame.image.load(os.path.join("images/rocket.png")),(100,100))
x = 400
y = 640

#enemy
enemy_ship = pygame.transform.scale(pygame.image.load(os.path.join("images/v_rocket.png")),(60,60))
enemyx = random.randint(0,800)
enemyy = 50

#bullet
f_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/f_ball.gif")),(30,30))
bulletX = 0
bulletY = y
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"

clock= pygame.time.Clock()

def rock(x,y):
	gameWindow.blit(rocket, (x,y))	# to display rocket on scree

def enemy(enemyx,enemyy):
	gameWindow.blit(enemy_ship, (enemyx,enemyy))

def bullet_f(x, y):
	global bullet_state
	bullet_state = "fire"
	gameWindow.blit(f_ball, (x + 35, y + 10))

def shoot(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 40:
        return True
    else:
        return False

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True

    if event.type==pygame.KEYDOWN:
	    if event.key == pygame.K_LEFT:
	    	x = x-7
	    	if x <= 0:
	    		x=0
	    	
	    elif event.key == pygame.K_RIGHT:
	    	x = x+7
	    	if x >= 800:
	    		x = 800

	    elif event.key == pygame.K_SPACE:
	    	if bullet_state == "ready":
	    		bulletX = x
	    		bullet_f(bulletX, bulletY)
	

    lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))  # create lives font
    Score_label = main_font.render(f"Score: {Score}", 1, (255,255,255)) # create Score font
    
    gameWindow.blit(background_image, [0,0])	# to display background image
    gameWindow.blit(lives_label, (10,10))	# to display lives on scree
    gameWindow.blit(Score_label, (width - Score_label.get_width() - 10, 10))	# to display Score on scree
    
    if bulletY <=0:
    	bulletY =y
    	bullet_state = "ready"

    if bullet_state == "fire":
        bullet_f(bulletX, bulletY)
        bulletY -= bulletY_change

    rock(x,y)
    enemyy += 2
    enemy(enemyx,enemyy)
    if enemyy == 800:
    	enemyx = random.randint(0,800)
    	enemyy = 50
    	lives -= 1
    if lives == 0:
    	break

    collision = shoot(enemyx, enemyy, bulletX, bulletY)
    if collision:
    	Score +=1
    	enemyx = random.randint(0,800)
    	enemyy = 50
    	bulletY = 480
    	bullet_state = "ready"

    if Score == 5:
    	fps = 500

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
quit()