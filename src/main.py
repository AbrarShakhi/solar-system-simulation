from sys import exit
print ('Hello world!')
try:
    from src.constant import COLOR, WINDOW, FACTOR, FONT, PHYSICS
    from src.object import Object as Obj
    from src.galaxy import get_objects, fill_stars, load_star
    import pygame
except:
    print("please run runme.py")
    exit(1)



class Main:
    def __init__(self, objects: list[Obj]) -> None:
        pygame.init()

        self.active = True
        self.pause = False
        self.FRAME_RATE = 120

        fonts = pygame.font.get_fonts()
        self.font = pygame.font.SysFont(fonts[0], FONT.SIZE, False, False)

        self.objects = objects
        self.stars = load_star()

        self.zoom_level = FACTOR.INIT_LEVEL

        self.FRAME = pygame.display.set_mode((WINDOW.MAIN_WIDTH, WINDOW.HEIGHT))
        pygame.display.set_caption("Solar System Simulation")

        self.clock = pygame.time.Clock()
        self.dt = 1


    def quit(self) -> None:
        pygame.quit()
        exit()


    def event(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.active = False
                self.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.pause = not self.pause
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.pause = not self.pause
                # elif e.key == pygame.K_UP or e.key == pygame.K_RIGHT:
                #     self.zoom_level += 1
                # elif e.key == pygame.K_DOWN or e.key == pygame.K_LEFT:
                #     self.zoom_level -= 1


    def update(self) -> None:
        self.clock.tick(self.FRAME_RATE)
        if FACTOR.DELTA_DIV != 0:
            self.dt = self.clock.get_time() / FACTOR.DELTA_DIV
        else:
            self.dt = 1
        pygame.display.update()


    def calc(self) -> None:
        max_dist_to_star = -1
        for obj in self.objects:
            obj.move(self.objects, self.dt, FACTOR.get_scale(self.zoom_level))
            if obj.dist_to_near_star > max_dist_to_star:
                max_dist_to_star = obj.dist_to_near_star
        self.zoom_level = ((min(WINDOW.WIDTH, WINDOW.HEIGHT) - 10) / 2) / FACTOR.get_scale(max_dist_to_star)
        if self.zoom_level > FACTOR.INIT_LEVEL:
            self.zoom_level = FACTOR.INIT_LEVEL


    def draw(self) -> None:
        self.FRAME.fill(COLOR.BLACK)

        fill_stars(self.FRAME, self.stars) #TODO

        text = self.font.render("distance to nearest star.", False, COLOR.WHITE, None)
        self.FRAME.blit(text, (WINDOW.WIDTH, 0))

        for i in range(0, len(self.objects)):
            self.objects[i].draw(self.FRAME, self.font, i+1, FACTOR.get_scale(self.zoom_level))

        text = self.font.render("press space to pause.", False, COLOR.WHITE, None)
        self.FRAME.blit(text, (WINDOW.WIDTH, WINDOW.HEIGHT - FONT.SIZE - 10))


    def run(self) -> None:
        while self.active:
            self.event()
            self.update()
            
            if not self.pause:
                self.calc()
                self.draw()
                self.collision()


    def collision(self) -> None:
        for o1 in self.objects:
            for o2 in self.objects:
                if o2 == o1:
                    continue
                else:
                    if o2.center.x == o1.center.x and o2.center.y == o1.center.y:
                        print(f"{o1.name} collided with {o2.name}")
                        self.pause = True
                        break


def main() -> None:
    main = Main(get_objects())
    main.run()
