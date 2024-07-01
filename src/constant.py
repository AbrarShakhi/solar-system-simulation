
class COLOR:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    SUN = (255, 242, 110)
    EARTH = (67, 158, 142)
    MARS = (246, 137, 1)
    VENUS = (200, 100, 80)

    MOON = (200, 200, 200)

class FONT:
    SIZE = 20


class WINDOW:
    WIDTH = 1200
    MAIN_WIDTH = WIDTH + 300
    HEIGHT = 1000


class PHYSICS:
    G = 6.67428e-11
    AU = 149.6e6 * 1000


class FACTOR:
    INIT_LEVEL = 300
    TIMESTEP = 3600 * 24
    DELTA_DIV = 0

    def get_scale(level):
        # if (level < 2):
        #     level = 1
        return level / PHYSICS.AU
        