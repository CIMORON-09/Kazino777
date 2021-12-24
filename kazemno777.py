import wrap
wrap.world.create_world(1000,800)


zifre=[1,2,3,4,5,6,7,8,9,10]
def kazinritapora():
    x = 150


    for did in zifre:
        x+=50
        if did == 10:
            x+=20
        wrap.sprite.add_text(str(did),x,650, text_color=(0, 123, 4),font_size=50,back_color=[255,12,0])







kazinritapora()
import wrap_py

wrap_py.app.start()
