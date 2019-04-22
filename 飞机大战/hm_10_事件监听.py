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
# screen.blit(hero, (200, 500))
# 可以在所有的图像绘制完成后 进行跟新
# pygame.display.update()

# 创建一个时钟对象
clock = pygame.time.Clock()
#  游戏循环，游戏的开始
# 1.定义rect记录给你的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)
while True:
    # 可以指定游戏循环内部执行的频率
    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:

        print(event_list)
    # 2 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 3 调用blit方法绘制图形
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 4 调用update方法跟新显示
    pygame.display.update()


pygame.quit()
