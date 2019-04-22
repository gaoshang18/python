import pygame

pygame.init()

# c创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0,0))
# pygame.display.update()
# 英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
# 可以在所有的图像绘制完成后 进行跟新
pygame.display.update()

while True:
    pass


pygame.quit()

