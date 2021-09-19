import pygame
import random
import threading

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

DIRECTIONS = ["NORTH", "WEST", "SOUTH", "EAST"]

SIZE = 32

class Tile:
    def __init__(self, posX, posY, obs=None):
        self.x = posX
        self.y = posY
        self.obstacle = obs

    def canSpawnHere(self):
        if self.obstacle is None:
            return True
        else:
            return False

    def getCoos(self):
        return self.x, self.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getObstacle(self):
        return self.obstacle

    def setObstacle(self, obstacle):
        self.obstacle = obstacle

    def canGoTo(self):
        if self.obstacle is None or self.obstacle.isRelic():
            return True
        else:
            return False

    def isTrollOnIt(self):
        if self.obstacle is not None and self.obstacle.getObstacle() == 2:
            return True
        return False

    def draw(self, window):
        color = WHITE
        pygame.draw.rect(window, color, pygame.Rect(self.x * SIZE, self.y * SIZE, SIZE, SIZE))
        if self.obstacle is not None:
            self.obstacle.draw(window, self.x, self.y)


class GameMap:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.tileList = []

        for x in range(0, sizeX):
            for y in range(0, sizeY):
                self.tileList.append(Tile(x, y))

        for tile in self.tileList:
            if tile.getObstacle() is None and 1 == random.randint(1, 10):
                tile.setObstacle(Obstacle(1))

        for tile in self.tileList:
            if tile.getObstacle() is None and 1 == random.randint(1, 20):
                tile.setObstacle(Obstacle(2))

    def getNewSpawnPoint(self):
        while True:
            tile = random.choice(self.tileList)
            if tile.canSpawnHere():
                return tile
        return None

    def getRelicPosX(self):
        for tile in self.tileList:
            if tile.getObstacle() is not None and tile.getObstacle().getObstacle() == 3:
                return tile.getX()

    def isTrollIn(self, tile):
        if tile is not None and tile.isTrollOnIt():
            return True
        return False

    def getRelicPosY(self):
        for tile in self.tileList:
            if tile.getObstacle() is not None and tile.getObstacle().getObstacle() == 3:
                return tile.getY()

    def getTileAt(self, x, y):
        for tile in self.tileList:
            if tile.getX() == x and tile.getY() == y:
                return tile
        return None

    def printMap(self, pl):
        mapToPrint = {}
        for t in self.tileList:
            x = t.getX()
            y = t.getY()
            if x in mapToPrint:
                mapToPrint[x][y] = t
            else:
                mapToPrint[x] = {y: t}

        toPrint = ""

        for y in mapToPrint:
            for x in mapToPrint[y]:
                if (x, y) == pl.getCoos():
                    toPrint += "H "
                else:
                    obs = mapToPrint[x][y].getObstacle()
                    if obs is not None:
                        toPrint += str(obs.getObstacle()) + " "
                    else:
                        toPrint += "0 "
            toPrint += "\n"

        print(toPrint)

    def drawMap(self, window):
        for t in self.tileList:
            t.draw(window)

class Harry:
    def __init__(self, direction):
        self.x = None
        self.y = None
        self.dir = direction
        self.game_map = None
        self.img = pygame.image.load("./harry.jpg")

    def getLookingAt(self):
        x = self.x
        y = self.y
        tile = None
        if self.dir == "NORTH":
            tile = self.game_map.getTileAt(x, y - 1)
        elif self.dir == "SOUTH":
            tile = self.game_map.getTileAt(x, y + 1)
        elif self.dir == "EAST":
            tile = self.game_map.getTileAt(x + 1, y)
        elif self.dir == "WEST":
            tile = self.game_map.getTileAt(x - 1, y)
        return tile

    def getDir(self):
        return self.dir

    def convertImg(self):
        self.img.convert()

    def rotateImage(self):
        self.image = self.img.copy()
        self.image = pygame.transform.rotate(self.image, (DIRECTIONS.index(self.dir) - 1) % 4 * 90)
        self.image.convert()

    def canMove(self):
        lookingAt = self.getLookingAt()
        if lookingAt is not None and lookingAt.canGoTo():
            return True
        else:
            return False

    def move(self):
        if self.canMove():
            if self.dir == "NORTH":
                self.y -= 1
            elif self.dir == "SOUTH":
                self.y += 1
            elif self.dir == "EAST":
                self.x += 1
            elif self.dir == "WEST":
                self.x -= 1

    def isOnTarget(self):
        if self.x == self.game_map.getRelicPosX() and self.y == self.game_map.getRelicPosY():
            return True
        else:
            return False

    def turn_right(self):
        self.dir = DIRECTIONS[(DIRECTIONS.index(self.dir) - 1) % len(DIRECTIONS)]

    def turn_left(self):
        self.dir = DIRECTIONS[(DIRECTIONS.index(self.dir) + 1) % len(DIRECTIONS)]

    def is_ennemy_in_front(self):
        if self.game_map.isTrollIn(self.getLookingAt()):
            return True
        else:
            return False

    def setGameMap(self, gMap):
        self.game_map = gMap

    def spawn(self):
        if self.game_map:
            self.x, self.y = self.game_map.getNewSpawnPoint().getCoos()

    def getCoos(self):
        return self.x, self.y

    def printMap(self):
        self.game_map.printMap(self)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def draw(self, scr):
        self.rotateImage()
        size = 32
        scr.blit(self.image, (self.x * size, self.y * size))


class Obstacle:
    def __init__(self, oType):
        self.type = oType
        if self.type == 1:
            self.image = pygame.image.load("./therock.png")
        elif self.type == 2:
            self.image = pygame.image.load("./troll.png")
        elif self.type == 3:
            self.image = pygame.image.load("./relic.png")

    def setObstacle(self, obs):
        self.type = obs
        if self.type == 1:
            self.image = pygame.image.load("./therock.png")
        elif self.type == 2:
            self.image = pygame.image.load("./troll.png")
        elif self.type == 3:
            self.image = pygame.image.load("./relic.png")

    def getObstacle(self):
        return self.type

    def isRelic(self):
        if self.type == 3:
            return True
        else:
            return False

    def draw(self, window, posX, posY):

        window.blit(self.image, (posX * SIZE, posY * SIZE))

game_map = GameMap(10, 10)
player = Harry(random.choice(DIRECTIONS))
player.setGameMap(game_map)
player.spawn()
relique = Obstacle(3)
game_map.getNewSpawnPoint().setObstacle(relique)


class App(threading.Thread):
    def __init__(self, gMap, pl, relic):
        threading.Thread.__init__(self)
        self.map = gMap
        self.player = pl
        self.relic = relic

        self.start()

    def run(self):
        pygame.init()

        size = (320, 320)
        self.window_surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Harry potter is dead !")
        clock = pygame.time.Clock()
        self.player.convertImg()
        carryOn = True
        # -------- Main Program Loop -----------
        while carryOn:
            # --- Drawing code should go here
            # First, clear the screen to white. 
            self.window_surface.fill(WHITE)
            # The you can draw different shapes and lines or add text to your background stage.
            game_map.drawMap(self.window_surface)
            player.draw(self.window_surface)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.update()
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False
                    pygame.quit()  # Flag that we are done so we exit this loop


app = App(game_map, player, relique)