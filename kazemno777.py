import random

import wrap

wrap.add_sprite_dir("fion")
wrap.world.create_world(1000, 800)
fon = wrap.sprite.add("foi", 500, 400, "fon")
fon = wrap.sprite.set_size(fon, 1000, 800)
ooe = wrap.sprite.add_text(" ", 500, 300, text_color=(0, 255, 4), font_size=50)
baraban_on = 0
gdkg = []
zifre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kolvomonet = 10
vipavshee_chislo=None


def kazinritapora():
    x = 200

    for did in zifre:
        x += 50
        if did == 10:
            x += 20
        id_sprite = wrap.sprite.add_text(str(did), x, 650, text_color=(0, 123, 4), font_size=50,
                                         back_color=[255, 12, 0])

        gdkg.append(id_sprite)


@wrap.always()
def vibor_zifor():
    global  vipavshee_chisl
    if baraban_on == 1:
        pervoe = zifre[4]
        vtoroe = zifre[4]

        vipavshee_chislo = random.randint(int(pervoe), int(vtoroe))
        wrap.sprite_text.set_text(ooe, str(vipavshee_chislo))
        print(vipavshee_chislo)

@wrap.on_key_down(wrap.K_SPACE)
def rererererere():
    global baraban_on
    if baraban_on == 0:
        baraban_on = 1
    else:

        baraban_on = 0


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def gyyggyggyg(pos_x, pos_y):
    for did in gdkg:
        global old,vipavshee_chislo,kolvomonet
        yre = wrap.sprite.is_collide_point(did, pos_x, pos_y)
        kolvomonet_id=wrap.sprite.add_text(str(kolvomonet), 180, 25, text_color=(0, 255, 4), font_size=30)
        wrap.sprite.add_text("МОНЕТЫ", 80, 25, text_color=(0, 255, 4), font_size=30)
        if yre == True:


            wrap.sprite_text.set_text_color(did, 0, 0, 255)
            wrap.sprite_text.set_text_color(old, 0, 123, 4)
            old = did


            if vipavshee_chislo==did :
                kolvomonet+=5
                wrap.sprite_text.set_text(kolvomonet_id,str(kolvomonet))





kazinritapora()
old = gdkg[0]
wrap.sprite_text.set_text_color(old, 0, 0, 255)

import wrap_py

wrap_py.app.start()
