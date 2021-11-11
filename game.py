import arcade

# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Star Wars"

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

        self.set_mouse_visible(False)


    # начальные значения
    def setup(self):
        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = 70
        self.player.angle = 100

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.center_x = x

    # отрисовка
    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background )
        self.player.draw()
    # игровая логика
    def update(self, delta_time):
        self.player.update()


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
