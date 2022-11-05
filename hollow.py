from circle import *
class Hollow(Circle):
    def __init__(self, screen, center_x, center_y, radius,  color='BLUE', background_color="WHITE"):
        super().__init__(screen, center_x, center_y, radius, color, background_color)
        self.var =1
    def draw(self):
        py.draw.circle(self.screen, self.color,super().get_center(), super().get_radius(),1)
        py.display.update()
    def remove(self):
        py.draw.circle(self.screen, self.bg, super().get_center(), super().get_radius(), self.var)
        py.display.update()
    def move(self, x, y):
        self.remove()
        super().set_center(x, y)
        self.draw()
    def change_size(self, val):
        self.remove()

        rad =super().get_radius()
        super().set_radius(rad +(rad * (val/100)))
        self.draw()

def main():
  
    screen = py.display.set_mode((800, 600))
    screen.fill('white')
    py.display.update()
    #line = Line(screen, 100, 100, 200, 200)
    holl = Hollow(screen, 450, 250, 50)
    holl.draw()
    sleep(1)
    holl.remove()
    sleep(1)
    holl.draw()
    sleep(1)
    holl.move(250, 150)
    sleep(1)
    holl.change_size(30)





main()