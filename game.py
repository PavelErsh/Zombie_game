import random

import arcade

# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Zombie"

class Zombie(arcade.AnimatedTimeSprite):
    def __init__(self):
        super().__init__()
        self.textures.append(arcade.load_texture("img//zombie0.png"))
        self.textures.append(arcade.load_texture("img//zombie1.png"))
        self.change_y = 1
        self.scale = 0.5
        self.angle = 260

    def update(self):
        self.center_y -= self.change_y

class Bullet(arcade.Sprite):
    def __init__(self):
        super(Bullet, self).__init__("img//bullet.png", 0.8)
        self.change_y = 10
        self.bullet_sound = arcade.load_sound("soud//sound.wav")

    def update(self):
        self.center_y += self.change_y
        if self.center_y > SCREEN_HEIGHT:
            self.kill()

class Player(arcade.Sprite):
    def update(self):
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0

# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("img//bacground.png")
        self.player = Player("img//player.png", 0.5)
        self.bullets = arcade.SpriteList()
        self.zombies = arcade.SpriteList()
        self.set_mouse_visible(False)


    # начальные значения
    def setup(self):
        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = 70
        self.player.angle = 100

        for i in range(50):
            zombie = Zombie()
            zombie.center_x = random.randint(20, SCREEN_WIDTH - 20)
            zombie.center_y = 100 * i

            self.zombies.append(zombie)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.center_x = x

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        bullet = Bullet()
        bullet.center_x = self.player.center_x
        bullet.bottom= self.player.top
        self.bullets.append(bullet)

    # отрисовка
    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background )
        self.player.draw()
        self.bullets.draw()
        self.zombies.draw()
    # игровая логика
    def update(self, delta_time):
        self.player.update()
        self.bullets.update()

        for bullet in self.bullets:
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()

        self.zombies.update_animation()
        self.zombies.update()


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
