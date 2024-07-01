try:
    import pygame
except:
    print("pygame is not installed.")
    print("please install pygame.")
    from sys import exit
    exit(1)
    

if __name__ == "__main__":
    import src.main as start
    start.main()
