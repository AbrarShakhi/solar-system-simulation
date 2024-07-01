from random import randint
from sys import exit
try:
    from src.constant import COLOR, PHYSICS, WINDOW
    from src.object import Object as Obj
    from src.object import Point
    import pygame
except:
    print("please run runme.py")
    exit(1)


def get_pos():
    return Point(randint(0, WINDOW.MAIN_WIDTH), randint(0, WINDOW.HEIGHT))

def load_star():
    number_of_star = int(min((WINDOW.WIDTH, WINDOW.HEIGHT)) // randint(25, 50))
    star_container = []
    while number_of_star > 0:
        number_of_star -= 1
        star_container.append(get_pos())
    return star_container


def fill_stars(win, star_container: list[Point]):
    for star in star_container: 
        pygame.draw.circle(win, COLOR.MOON, (star.x, star.y), 3)

    if randint(1, 100) % 10 == 0:
        number_of_star = len(star_container)
        if number_of_star > 0:
            dice = randint(1, number_of_star) % number_of_star
            star_container.pop(dice)
        star_container.append(get_pos())




def get_objects() -> list[Obj]:
    SUN_MASS = 1.98892*10**30
    EARTH_MASS = 5.9742*10**24
    MARS_MASS = 6.39*10**23
    VENUS_MASS = 4.8685*10**24
    MERCURY_MASS = 3.30*10**23

    objects: list[Obj] = []
    objects.append(Obj("sun", Point(0, 0), 30, SUN_MASS, COLOR.SUN, Point(0,0), True))
    objects.append(Obj("earth", Point(-1 * PHYSICS.AU, 0), 16, EARTH_MASS, COLOR.EARTH, Point(0, 29.783*1000), False))
    objects.append(Obj("mars", Point(-1.524 * PHYSICS.AU, 0), 12, MARS_MASS, COLOR.MARS, Point(0, 24.077*1000), False))
    objects.append(Obj("venus", Point(0.723 * PHYSICS.AU, 0), 14, VENUS_MASS, COLOR.VENUS, Point(0, -35.02*1000), False))
    objects.append(Obj("mercury", Point(0.387 * PHYSICS.AU, 0), 8, MERCURY_MASS, COLOR.MOON, Point(0, -47.4*1000), False))

    return objects
