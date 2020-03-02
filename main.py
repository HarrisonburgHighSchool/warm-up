import pyglet
from util import *

win = pyglet.window.Window()
# Load the image & create the sprite
img = pyglet.image.load('assets/gfx/Inner.png')
img = img.get_region(x=0, y=384, width=16, height=16)

# Make the sprites
spr1 = pyglet.sprite.Sprite(img, x = 0, y = 0)
spr2 = pyglet.sprite.Sprite(img, x = 40, y = 50)
spr1.scale = 4
spr2.scale = 4

def update(dt):
  pass

@win.event
def on_draw():
  win.clear()
  pixelScale()

  spr1.draw()
  spr2.draw()

pyglet.clock.schedule_interval(update, 0.015)
pyglet.app.run()

