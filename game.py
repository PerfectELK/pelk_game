import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Pelk huelk')

x = 50
y = 425

clock = pygame.time.Clock()

width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
last_move = 'right'

walkRight = [pygame.image.load('sprites/pygame_right_1.png'), pygame.image.load('sprites/pygame_right_2.png'), pygame.image.load('sprites/pygame_right_3.png'), pygame.image.load('sprites/pygame_right_4.png'), pygame.image.load('sprites/pygame_right_5.png'), pygame.image.load('sprites/pygame_right_6.png')]

walkLeft = [pygame.image.load('sprites/pygame_left_1.png'), pygame.image.load('sprites/pygame_left_2.png'), pygame.image.load('sprites/pygame_left_3.png'), pygame.image.load('sprites/pygame_left_4.png'), pygame.image.load('sprites/pygame_left_5.png'), pygame.image.load('sprites/pygame_left_6.png')]

bg = pygame.image.load('sprites/pygame_bg.jpg')
playerStand = pygame.image.load('sprites/pygame_idle.png')


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


class Bullet:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)




run = True
bullets = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if last_move == 'right':
            facing = 1
        else:
            facing = -1
        if len(bullets) < 100:
            bullets.append(Bullet(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        last_move = 'left'
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
        last_move = 'right'
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += jumpCount ** 2 / 2
            else:
                y -= jumpCount ** 2 / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()




pygame.quit()