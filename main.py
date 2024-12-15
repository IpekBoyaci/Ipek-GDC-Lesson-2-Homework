import pgzrun
import random

TITLE="Get The Cat To the Food"

WIDTH=400
HEIGHT=400

#creating a new character(actor) in pygame
cat=Actor('cat')
cat.pos=50,50
cat.scale=0.25
catfood=Actor('catfood')
catfood.pos=50,100
catfood.scale=0.25
message="Game is Starting!"

def draw():
    screen.clear()
    screen.fill("pink")
    cat.draw()
    catfood.draw()
    screen.draw.text(message,center=(200,20), fontsize=30, color="black")

def place_cat():
    cat.x=random.randint(50,350)
    cat.y=random.randint(50,350)

def place_catfood():
    catfood.x=random.randint(50,350)
    catfood.y=random.randint(50,350)

#on_mouse_down - in built function which gets triggered, when you click on the game screen
def on_mouse_down(pos):
    global message
    #collidepoint- inbuilt function -checks collision between mouse pointer and actor
    if catfood.collidepoint(pos):
        message="Good Job!"
        cat.x=catfood.x
        cat.y=catfood.y 
        place_catfood()   
    else:
        message="Try again!"
#place_alien function before pgzrun to place the alien at a random position at the start        
place_cat()
place_catfood()
pgzrun.go()