import pygame
pygame.mixer.init()
#CONFIGURACION DE PANTALLA----------------
WIDTH = 1320
HEIGHT = 560
SIZE_SCREEN = (WIDTH, HEIGHT)
#UBICACIONES EN PANTALLA-----------------
ORIGIN = (0, 0)
DISPLAY_TOP = 0
DISPLAY_BOTTOM = HEIGHT
DISPLAY_LEFT = 0
DISPLAY_RIGHT = WIDTH
DISPLAY_CENTER_X = WIDTH // 2
DISPLAY_CENTER_Y = HEIGHT // 2
DISPLAY_MIDTOP = (DISPLAY_CENTER_X, DISPLAY_TOP)
DISPLAY_CENTER = (DISPLAY_CENTER_X, DISPLAY_CENTER_Y)
# COLORES --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (238, 130, 238)
DARK_GREEN = (0, 100, 0)
PINK = (255, 192, 203)
TURQUOISE = (64, 224, 208)
GREY = (128, 128, 128)
PALE_YELLOW = (255, 255, 153)
BROWN = (139, 69, 19)
# FPS----------------------
FPS = 60
SPEED = 5
SPEED_JUMP_PLAYER = -15
# ///////////////////////////////////////
lista_superficie = [(0, 514, 1320, 44),
                    (0, 410, 170, 15),
                    (230, 410, 327, 15),
                    (230, 265, 327, 15),
                    (230, 142, 327, 18),
                    (622, 451, 288, 20),
                    (643, 390, 207, 10),
                    (918, 416, WIDTH - 920, 15),
                    (918, 333, WIDTH - 920, 15),
                    (918, 249, WIDTH - 920, 15)
]

# ///////////////////////////////////////////////////////////////////////////////
menu_items = [
    {
        'text': 'play',
        'position': (WIDTH // 2, HEIGHT // 2),
        'normal_color': WHITE,
        'hover_color': GREEN
    },
    {
        'text': 'exit',
        'position': (WIDTH // 2, HEIGHT // 2 + 100),
        'normal_color': WHITE,
        'hover_color': RED
    }
]
game_over_items = [
    {
        "text": "try again",
        "position": (400, 400),
        "normal_color": WHITE,
        "hover_color": GREEN
    },
    {
        "text": "EXIT",
        "position": (1000, 400),
        "normal_color": WHITE,
        "hover_color": RED
    }
]

level_item = [
    {
        "text": "LEVEL 1",
        "position": (WIDTH // 2, HEIGHT // 2 - 100),
        "normal_color": WHITE,
        "hover_color": GREEN
    },
    {
        "text": "LEVEL 2",
        "position": (WIDTH // 2, HEIGHT // 2),
        "normal_color": WHITE,
        "hover_color": GREEN
    },
    {
        "text": "LEVEL 3",
        "position": (WIDTH // 2, HEIGHT // 2 + 100),
        "normal_color": WHITE,
        "hover_color": GREEN
    },
    {
        "text": "BACK",
        "position": (WIDTH // 2, HEIGHT // 2 + 200),
        "normal_color": WHITE,
        "hover_color": GREEN
    }
]
pause_items = [
    {
        'text': 'REANUDE',
        'position': (WIDTH // 2, HEIGHT // 2),
        'normal_color': WHITE,
        'hover_color': GREEN
    },
    {
        'text': 'EXIT',
        'position': (WIDTH // 2, HEIGHT // 2 + 100),
        'normal_color': WHITE,
        'hover_color': RED
    }
]


game_win_items = [
    {
        "text": "AGAIN GAME",
        "position": (400, 400),
        "normal_color": WHITE,
        "hover_color": GREEN
    },
    {
        "text": "EXIT",
        "position": (1000, 400),
        "normal_color": WHITE,
        "hover_color": RED
    }
]
