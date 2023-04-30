import pygame.mouse
from pygame import*

init()

info = display.Info()

WIDTH = info.current_w
HEIGHT = info.current_h

clock = time.Clock()
FPS = 60

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Novela")
background = transform.scale(image.load("image/galaxy.jpg"), (WIDTH, HEIGHT))


class Button:
    def __int__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)

    def button_color_draw(self, x, y, message, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y +self.height:
            pygame.button_color_draw.rect(display, self.active_color, (x, y, self.width, self.height))

            if click[0] == 1 and action is not None:
                action()


        else:
            pygame.button_color_draw.rect(display, self.inactive_color, (x, y, self.width, self.height))

        print_text(message, x + 10, y + 10)



def print_text(message, x, y, font_color = (0, 0, 0), font_type = "Alkalami-Regular.ttf", font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))



button_menu = Button(100, 50)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

    button_menu.button_color_draw(20, 100, "Play")

    window.blit(background, (0, 0))
    display.update()
    clock.tick(FPS)