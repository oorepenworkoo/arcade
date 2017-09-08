import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SpaceGameWindow(arcade.Window):
    i = 0
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.ship = arcade.Sprite('images/ship.png')
        self.ship.set_position(width/2,height/6)

    def on_draw(self):
        arcade.start_render()

        self.ship.draw()

    def update(self, delta):
        ship = self.ship
        if ship.center_y > SCREEN_HEIGHT:
            ship.center_y = 0
        self.ship.set_position(self.ship.center_x,self.ship.center_y+delta*SpaceGameWindow.i)
        SpaceGameWindow.i+=1

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
