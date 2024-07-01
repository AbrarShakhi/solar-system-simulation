from sys import exit
try:
    from src.constant import COLOR, WINDOW, PHYSICS, FACTOR, FONT
    import pygame, math
except:
    print("please run runme.py")
    exit(1)



class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def scalify(self, scale)-> tuple:
        x = self.x * scale + WINDOW.WIDTH / 2
        y = self.y * scale + WINDOW.HEIGHT / 2
        return x, y


class Object:
    def __init__(self, name: str, center: Point, radius, mass, color: COLOR, init_velocity: Point, is_star: bool) -> None:
        self.center = center
        self.radius = radius
        self.mass = mass
        self.color = color
        self.name = name

        self.orbit: list[Point] = []

        self.is_star = is_star
        self.dist_to_near_star = 0

        self.velocity = init_velocity


    def draw(self, frame:pygame.Surface, font: pygame.font, nth, scale) -> None:

        x, y = self.center.scalify(scale)

        if len(self.orbit) > 1:
            lines = []
            for ce in self.orbit:
                lines.append(ce.scalify(scale))

            pygame.draw.lines(frame, COLOR.WHITE, False, lines, 1)

        pygame.draw.circle(frame, self.color, (x, y), self.radius)

        text = font.render(self.name, False, COLOR.WHITE, COLOR.BLACK)
        frame.blit(text, (x, y))
        
        text = font.render(f"{self.name}: {round(self.dist_to_near_star/PHYSICS.AU, 8)} AU", False, COLOR.WHITE, COLOR.BLACK)
        frame.blit(text, (WINDOW.WIDTH, (FONT.SIZE + 6) * nth))


    def attraction(self, relative_obj) -> Point:
        dist_point = Point(relative_obj.center.x - self.center.x, relative_obj.center.y - self.center.y)
        d = math.sqrt(dist_point.x**2 + dist_point.y**2)

        if relative_obj.is_star:
            self.dist_to_near_star = d

        F = PHYSICS.G * (self.mass * relative_obj.mass) / (d ** 2) # F = G(Mm)/(r^2)

        theta = math.atan2(dist_point.y, dist_point.x) # tanA = y/x
        Fx = F * math.cos(theta) # x = rcosA
        Fy = F * math.sin(theta) # y = rsinA

        return Point(Fx, Fy)


    def move(self, objects, dt, scale) -> None:
        # dt = 1

        F = Point(0, 0)
        for obj in objects:
            if obj != self:
                f = self.attraction(obj)
                F.x += f.x
                F.y += f.y
        
        # F = ma, 
        # a = F/m
        self.velocity.x += F.x / self.mass * dt * FACTOR.TIMESTEP
        self.velocity.y += F.y / self.mass * dt * FACTOR.TIMESTEP

        self.center.x += self.velocity.x * dt * FACTOR.TIMESTEP
        self.center.y += self.velocity.y * dt * FACTOR.TIMESTEP

        self.orbit.append(Point(self.center.x, self.center.y))

        length = len(self.orbit)
        if length > math.pi * (self.dist_to_near_star * scale) or length > 1000:
            self.orbit.pop(0)






