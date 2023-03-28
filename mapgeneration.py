import pygame
from opensimplex import OpenSimplex
import os
import time
import numpy as np


# Initialize Pygame
pygame.init()

# Define the size of the graph and the scale of the noise
width = 1920
height = 1000
scale = 100.0
world_length = 256
block_size = 80
# Create an instance of the OpenSimplex class
noise = OpenSimplex(17823461897361)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("OpenSimplex 1D Graph")

codepath = os.getcwd()
dirtpath = codepath + r'\textures\dirt.png'
grasspath = codepath + r'\textures\grass.png'
stonepath = codepath + r'\textures\stone.png'
fontpath = codepath + r'\textures\Font.font'
water1path = codepath + r'\textures\water1.png'
water2path = codepath + r'\textures\water2.png'
water3path = codepath + r'\textures\water3.png'
water4path = codepath + r'\textures\water4.png'
water5path = codepath + r'\textures\water5.png'
water6path = codepath + r'\textures\water6.png'
water7path = codepath + r'\textures\water7.png'

gamebackgroundpath = codepath + r'\textures\gamebackground.png'
gamebackground = pygame.image.load(gamebackgroundpath).convert()


imagegame_width, imagegame_height = gamebackground.get_size()

game_factor = max(width/imagegame_width, height/imagegame_height)

scaledgame_width = int(imagegame_width * game_factor)
scaledgame_height = int(imagegame_height * game_factor)
gamebackground = pygame.transform.scale(gamebackground, (scaledgame_width, scaledgame_height))

x_pos = int((width - scaledgame_width) / 2)
y_pos = int((height - scaledgame_height) / 2)




def changeBrightness(image, brightness):
    image_array = pygame.surfarray.array3d(image)

    image_array = image_array * brightness

    np.clip(image_array, 0, 255, out=image_array)
    
    return pygame.surfarray.make_surface(image_array)


def write(text, x, y, color="grey",):
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(x, y))
    return text, text_rect

class getFPS:
    def __init__(self):
        self.timesList = [0.01, 0.01, 0.01, 0.01, 0.01]
        self.pos = 0
        self.startTime = time.time()
    def FPS(self):
        tempFPS = time.time() - self.startTime
        try:
            tempFPS = 1/tempFPS
        except ZeroDivisionError:
            tempFPS = 1000
        self.timesList[self.pos] = tempFPS
        self.startTime = time.time()
        self.pos += 1
        if self.pos == 5:
            self.pos = 0
        fps = self.timesList[0]
        fps += self.timesList[1]
        fps += self.timesList[2]
        fps += self.timesList[3]
        fps += self.timesList[4]
        fps = fps/5
        return fps


font = pygame.font.Font(fontpath, 29)
clock = pygame.time.Clock()
FPS = 75



class Chunk:
    def __init__(self, xy) -> None:
        self.xy = xy
        self.chunk=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class Render:
    def __init__(self) -> None:
        self.scroll = 0
        self.time = 1
        self.brightness = 1
        self.frameCount = 0
        self.scrollver = 0
        self.waterPos = 0
        self.amount = block_size*16
        self.screensize = (width + block_size*15, height + block_size*15)
        self.land = pygame.image.load(dirtpath).convert()
        self.grass = pygame.image.load(grasspath).convert()
        self.stone = pygame.image.load(stonepath).convert()
        self.water1 = pygame.image.load(water1path).convert()
        self.water2 = pygame.image.load(water2path).convert()
        self.water3 = pygame.image.load(water3path).convert()
        self.water4 = pygame.image.load(water4path).convert()
        self.water5 = pygame.image.load(water5path).convert()
        self.water6 = pygame.image.load(water6path).convert()
        self.water7 = pygame.image.load(water7path).convert()
        self.land = pygame.transform.scale(self.land, (block_size , block_size))
        self.grass = pygame.transform.scale(self.grass, (block_size , block_size))
        self.stone = pygame.transform.scale(self.stone, (block_size , block_size))
        self.water1 = pygame.transform.scale(self.water1, (block_size , block_size))
        self.water2 = pygame.transform.scale(self.water2, (block_size , block_size))
        self.water3 = pygame.transform.scale(self.water3, (block_size , block_size))
        self.water4 = pygame.transform.scale(self.water4, (block_size , block_size))
        self.water5 = pygame.transform.scale(self.water5, (block_size , block_size))
        self.water6 = pygame.transform.scale(self.water6, (block_size , block_size))
        self.water7 = pygame.transform.scale(self.water7, (block_size , block_size))

        self.landtemp = pygame.image.load(dirtpath).convert()
        self.grasstemp = pygame.image.load(grasspath).convert()
        self.stonetemp = pygame.image.load(stonepath).convert()
        self.water1temp = pygame.image.load(water1path).convert()
        self.water2temp = pygame.image.load(water2path).convert()
        self.water3temp = pygame.image.load(water3path).convert()
        self.water4temp = pygame.image.load(water4path).convert()
        self.water5temp = pygame.image.load(water5path).convert()
        self.water6temp = pygame.image.load(water6path).convert()
        self.water7temp = pygame.image.load(water7path).convert()
        self.landtemp = pygame.transform.scale(self.landtemp, (block_size , block_size))
        self.grasstemp = pygame.transform.scale(self.grasstemp, (block_size , block_size))
        self.stonetemp = pygame.transform.scale(self.stonetemp, (block_size , block_size))
        self.water1temp = pygame.transform.scale(self.water1temp, (block_size , block_size))
        self.water2temp = pygame.transform.scale(self.water2temp, (block_size , block_size))
        self.water3temp = pygame.transform.scale(self.water3temp, (block_size , block_size))
        self.water4temp = pygame.transform.scale(self.water4temp, (block_size , block_size))
        self.water5temp = pygame.transform.scale(self.water5temp, (block_size , block_size))
        self.water6temp = pygame.transform.scale(self.water6temp, (block_size , block_size))
        self.water7temp = pygame.transform.scale(self.water7temp, (block_size , block_size))

        self.landtemptemp = pygame.image.load(dirtpath).convert()
        self.grasstemptemp = pygame.image.load(grasspath).convert()
        self.stonetemptemp = pygame.image.load(stonepath).convert()
        self.water1temptemp = pygame.image.load(water1path).convert()
        self.water2temptemp = pygame.image.load(water2path).convert()
        self.water3temptemp = pygame.image.load(water3path).convert()
        self.water4temptemp = pygame.image.load(water4path).convert()
        self.water5temptemp = pygame.image.load(water5path).convert()
        self.water6temptemp = pygame.image.load(water6path).convert()
        self.water7temptemp = pygame.image.load(water7path).convert()
        self.landtemptemp = pygame.transform.scale(self.landtemptemp, (block_size , block_size))
        self.grasstemptemp = pygame.transform.scale(self.grasstemptemp, (block_size , block_size))
        self.stonetemptemp = pygame.transform.scale(self.stonetemptemp, (block_size , block_size))
        self.water1temptemp = pygame.transform.scale(self.water1temptemp, (block_size , block_size))
        self.water2temptemp = pygame.transform.scale(self.water2temptemp, (block_size , block_size))
        self.water3temptemp = pygame.transform.scale(self.water3temptemp, (block_size , block_size))
        self.water4temptemp = pygame.transform.scale(self.water4temptemp, (block_size , block_size))
        self.water5temptemp = pygame.transform.scale(self.water5temptemp, (block_size , block_size))
        self.water6temptemp = pygame.transform.scale(self.water6temptemp, (block_size , block_size))
        self.water7temptemp = pygame.transform.scale(self.water7temptemp, (block_size , block_size))
    
    def render(self, chunk) -> None:
        if self.time == 100000:
            if self.waterPos < 6:
                self.waterPos +=1
            else:
                self.waterPos = 0
            self.time = 0
        self.time += 1
        self.amount = block_size*16
        x, y = chunk.xy
        x = x*self.amount
        y = y*self.amount
        scrolledx = x + self.scroll
        scrolledy = y + self.scrollver
        amount = block_size*8
        if scrolledx > -amount and scrolledx < width + amount and scrolledy > -amount and scrolledy < height + amount:
            chunkx = -amount
            chunky = -amount
            for _ in chunk.chunk:
                for land in _:
                    if land == 11:
                        window.blit(self.land, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                    if land == 111:
                        window.blit(self.grass, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                    if land == 1111:
                        window.blit(self.stone, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                    if land == 11111:
                        if self.waterPos == 0:
                            window.blit(self.water1, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                        if self.waterPos == 1:
                            window.blit(self.water2, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                        if self.waterPos == 2:
                            window.blit(self.water3, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                        if self.waterPos == 3:
                            window.blit(self.water4, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                        if self.waterPos == 4:
                            window.blit(self.water5, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                        if self.waterPos == 5:
                            window.blit(self.water6, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                        if self.waterPos == 6:
                            window.blit(self.water7, (x + self.scroll + chunkx ,  y + self.scrollver + chunky))
                    if land == 1:
                        pass
                    chunkx+=block_size
                chunkx=-amount
                chunky+=block_size

    def changeBrightness(self, brightness):
        image = self.landtemp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.land = pygame.surfarray.make_surface(image_array)

        image = self.grasstemp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.grass = pygame.surfarray.make_surface(image_array)

        image = self.stonetemp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)

        self.stone = pygame.surfarray.make_surface(image_array)



        image = self.water1temp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.water1 = pygame.surfarray.make_surface(image_array)



        image = self.water2temp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.water2 = pygame.surfarray.make_surface(image_array)
        

        image = self.water3temp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.water3 = pygame.surfarray.make_surface(image_array)
        

        image = self.water4temp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.water4 = pygame.surfarray.make_surface(image_array)
        

        image = self.water5temp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.water5 = pygame.surfarray.make_surface(image_array)
        

        image = self.water6temp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.water6 = pygame.surfarray.make_surface(image_array)

        image = self.water7temp
        image_array = pygame.surfarray.array3d(image)

        image_array = image_array * brightness

        np.clip(image_array, 0, 255, out=image_array)
    
        self.water7 = pygame.surfarray.make_surface(image_array)


        



render = Render()


def generateChunk(input, offset, height):
    listOfCords = []
    for i in range(16):
        noise_value = noise.noise2((i+offset)/scale, 0.6)
        listOfCords.append((noise_value*0.04) + 0.072)

    for y in range(16):
        for x in range(16):
            value = listOfCords[x] - height
            if y == 0 and value >= 0.016:
                input.chunk[y][x] = 11
            if y == 1 and value >= 0.015:
                input.chunk[y][x] = 11
            if y == 2 and value >= 0.014:
                input.chunk[y][x] = 11
            if y == 3 and value >= 0.013:
                input.chunk[y][x] = 11
            if y == 4 and value >= 0.012:
                input.chunk[y][x] = 11
            if y == 5 and value >= 0.011:
                input.chunk[y][x] = 11
            if y == 6 and value >= 0.010:
                input.chunk[y][x] = 11
            if y == 7 and value >= 0.009:
                input.chunk[y][x] = 11
            if y == 8 and value >= 0.008:
                input.chunk[y][x] = 11
            if y == 9 and value >= 0.007:
                input.chunk[y][x] = 11
            if y == 10 and value >= 0.006:
                input.chunk[y][x] = 11
            if y == 11 and value >= 0.005:
                input.chunk[y][x] = 11
            if y == 12 and value >= 0.004:
                input.chunk[y][x] = 11
            if y == 13 and value >= 0.003:
                input.chunk[y][x] = 11
            if y == 14 and value >= 0.002:
                input.chunk[y][x] = 11
            if y == 15 and value >= 0.001:
                input.chunk[y][x] = 11

            if y == 0 and value >= 0.016 and value <= 0.017:
                input.chunk[y][x] = 111
            if y == 1 and value >= 0.015 and value <= 0.016:
                input.chunk[y][x] = 111
            if y == 2 and value >= 0.014 and value <= 0.015:
                input.chunk[y][x] = 111
            if y == 3 and value >= 0.013 and value <= 0.014:
                input.chunk[y][x] = 111
            if y == 4 and value >= 0.012 and value <= 0.013:
                input.chunk[y][x] = 111
            if y == 5 and value >= 0.011 and value <= 0.012:
                input.chunk[y][x] = 111
            if y == 6 and value >= 0.010 and value <= 0.011:
                input.chunk[y][x] = 111
            if y == 7 and value >= 0.009 and value <= 0.010:
                input.chunk[y][x] = 111
            if y == 8 and value >= 0.008 and value <= 0.009:
                input.chunk[y][x] = 111
            if y == 9 and value >= 0.007 and value <= 0.008:
                input.chunk[y][x] = 111
            if y == 10 and value >= 0.006 and value <= 0.007:
                input.chunk[y][x] = 111
            if y == 11 and value >= 0.005 and value <= 0.006:
                input.chunk[y][x] = 111
            if y == 12 and value >= 0.004 and value <= 0.005:
                input.chunk[y][x] = 111
            if y == 13 and value >= 0.003 and value <= 0.004:
                input.chunk[y][x] = 111
            if y == 14 and value >= 0.002 and value <= 0.003:
                input.chunk[y][x] = 111
            if y == 15 and value >= 0.001 and value <= 0.002:
                input.chunk[y][x] = 111

            if y == 0 and value >= 0.020:
                input.chunk[y][x] = 1111
            if y == 1 and value >= 0.019:
                input.chunk[y][x] = 1111
            if y == 2 and value >= 0.018:
                input.chunk[y][x] = 1111
            if y == 3 and value >= 0.017:
                input.chunk[y][x] = 1111
            if y == 4 and value >= 0.016:
                input.chunk[y][x] = 1111
            if y == 5 and value >= 0.015:
                input.chunk[y][x] = 1111
            if y == 6 and value >= 0.014:
                input.chunk[y][x] = 1111
            if y == 7 and value >= 0.013:
                input.chunk[y][x] = 1111
            if y == 8 and value >= 0.012:
                input.chunk[y][x] = 1111
            if y == 9 and value >= 0.011:
                input.chunk[y][x] = 1111
            if y == 10 and value >= 0.010:
                input.chunk[y][x] = 1111
            if y == 11 and value >= 0.009:
                input.chunk[y][x] = 1111
            if y == 12 and value >= 0.008:
                input.chunk[y][x] = 1111
            if y == 13 and value >= 0.007:
                input.chunk[y][x] = 1111
            if y == 14 and value >= 0.006:
                input.chunk[y][x] = 1111
            if y == 15 and value >= 0.005:
                input.chunk[y][x] = 1111

            h = height - y*0.001
            if h < 0.04:
                if input.chunk[y][x] == 1:
                    input.chunk[y][x] = 11111

chunkseeeehigh = []
chunkseeehigh = []
chunkseehigh = []
chunksehigh = []
chunkshigh = []
chunksmid = []
chunkslow = []
chunkselow = []
chunkseelow = []
chunkseeelow = []
amount = block_size*16

genPos = 0
for i in range(world_length):
    chunkseeeehigh.append(Chunk((genPos, -4)))
    genPos+=1

genPos = 0
for i in range(world_length):
    chunkseeehigh.append(Chunk((genPos, -3)))
    genPos+=1

genPos = 0
for i in range(world_length):
    chunkseehigh.append(Chunk((genPos, -2)))
    genPos+=1

genPos = 0
for i in range(world_length):
    chunksehigh.append(Chunk((genPos, -1)))
    genPos+=1

genPos = 0
for i in range(world_length):
    chunkshigh.append(Chunk((genPos, 0)))
    genPos+=1

genPos = 0
for i in range(world_length):
    chunksmid.append(Chunk((genPos, 1)))
    genPos+=1

genPos = 0
for i in range(world_length):
    chunkslow.append(Chunk((genPos, 2)))
    genPos+=1

genPos = 0
for i in range(world_length):
    chunkselow.append(Chunk((genPos, 3)))
    genPos+=1
genPos = 0
for i in range(world_length):
    chunkseelow.append(Chunk((genPos, 4)))
    genPos+=1

num = 0

for chunk in chunkseeeehigh:
    generateChunk(chunk, num, 0.128)
    num+=16

num = 0

for chunk in chunkseeehigh:
    generateChunk(chunk, num, 0.112)
    num+=16

num = 0

for chunk in chunkseehigh:
    generateChunk(chunk, num, 0.096)
    num+=16

num = 0
for chunk in chunksehigh:
    generateChunk(chunk, num, 0.080)
    num+=16

num = 0
for chunk in chunkshigh:
    generateChunk(chunk, num, 0.064)
    num+=16

num = 0
for chunk in chunksmid:
    generateChunk(chunk, num, 0.048)
    num+=16

num = 0
for chunk in chunkslow:
    generateChunk(chunk, num, 0.032)
    num+=16

num = 0
for chunk in chunkselow:
    generateChunk(chunk, num, 0.016)
    num+=16

num = 0
for chunk in chunkseelow:
    generateChunk(chunk, num, 0.0)
    num+=16

fps = getFPS()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(gamebackground, (x_pos, y_pos))

    for chunk in chunkseeeehigh:
        render.render(chunk)
    for chunk in chunkseeehigh:
        render.render(chunk)
    for chunk in chunkseehigh:
        render.render(chunk)
    for chunk in chunksehigh:
        render.render(chunk)
    for chunk in chunkshigh:
        render.render(chunk)
    for chunk in chunksmid:
        render.render(chunk)
    for chunk in chunkslow:
        render.render(chunk)
    for chunk in chunkselow:
        render.render(chunk)
    for chunk in chunkseelow:
        render.render(chunk)  
    
          
    
    text = font.render("FPS: "+str(int(fps.FPS())), 1, pygame.Color('black'))
    window.blit(text, (width - 150, height - 50))
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        render.scroll += 15
    if keys[pygame.K_RIGHT]:
        render.scroll -= 15
    if keys[pygame.K_UP]:
        render.scrollver += 15
    if keys[pygame.K_DOWN]:
        render.scrollver -= 15
    if keys[pygame.K_w]:
        render.brightness += 0.01
        render.changeBrightness(render.brightness)
    if keys[pygame.K_s]:
        render.brightness -= 0.01
        render.changeBrightness(render.brightness)
    if keys[pygame.K_a]:
        block_size += 1
        amount = block_size*16
        render.landtemp = pygame.transform.scale(render.landtemptemp, (block_size , block_size))
        render.grasstemp = pygame.transform.scale(render.grasstemptemp, (block_size , block_size))
        render.stonetemp = pygame.transform.scale(render.stonetemptemp, (block_size , block_size))
        render.water1temp = pygame.transform.scale(render.water1temptemp, (block_size , block_size))
        render.water2temp = pygame.transform.scale(render.water2temptemp, (block_size , block_size))
        render.water3temp = pygame.transform.scale(render.water3temptemp, (block_size , block_size))
        render.water4temp = pygame.transform.scale(render.water4temptemp, (block_size , block_size))
        render.water5temp = pygame.transform.scale(render.water5temptemp, (block_size , block_size))
        render.water6temp = pygame.transform.scale(render.water6temptemp, (block_size , block_size))
        render.water7temp = pygame.transform.scale(render.water7temptemp, (block_size , block_size))
        render.changeBrightness(render.brightness)

    if keys[pygame.K_d]:
        if block_size > 2:
            block_size -= 1
            amount = block_size*16
            render.landtemp = pygame.transform.scale(render.landtemptemp, (block_size , block_size))
            render.grasstemp = pygame.transform.scale(render.grasstemptemp, (block_size , block_size))
            render.stonetemp = pygame.transform.scale(render.stonetemptemp, (block_size , block_size))
            render.water1temp = pygame.transform.scale(render.water1temptemp, (block_size , block_size))
            render.water2temp = pygame.transform.scale(render.water2temptemp, (block_size , block_size))
            render.water3temp = pygame.transform.scale(render.water3temptemp, (block_size , block_size))
            render.water4temp = pygame.transform.scale(render.water4temptemp, (block_size , block_size))
            render.water5temp = pygame.transform.scale(render.water5temptemp, (block_size , block_size))
            render.water6temp = pygame.transform.scale(render.water6temptemp, (block_size , block_size))
            render.water7temp = pygame.transform.scale(render.water7temptemp, (block_size , block_size))
            render.changeBrightness(render.brightness)

    #clock.tick(FPS)
    
# Quit Pygame
pygame.quit()
