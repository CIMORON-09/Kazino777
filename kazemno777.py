import random

import wrap
wrap.add_sprite_dir("fion")
wrap.world.create_world(1000,800)
fon=wrap.sprite.add("foi",500,400,"fon")
fon=wrap.sprite.set_size(fon,1000,800)


zifre=[1,2,3,4,5,6,7,8,9,10]
@wrap.on_mouse_down(1)
def kazinritapora(pos_x,pos_y):
    x = 200

    wrap.sprite.add_text("МОНЕТЫ",80,25, text_color = (0, 255, 4), font_size =30)


    wrap.sprite.add_text("10",180,25, text_color=(0, 255, 4), font_size=30)


    for did in zifre:
        x+=50
        if did == 10:
            x+=20
        wrap.sprite.add_text(str(did),x,650, text_color=(0, 123, 4),font_size=50,back_color=[255,12,0])


        pervoe=zifre[1]
        vtoroe=zifre[-1]
        kol=random.randint(int(pervoe),int(vtoroe))
        wrap.sprite.add_text(str(kol),500,500 ,text_color=(0, 255, 4), font_size=30)






import wrap_py

wrap_py.app.start()
