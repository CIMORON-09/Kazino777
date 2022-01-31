import random

import wrap

wrap.add_sprite_dir("fion")
wrap.world.create_world(1000, 800)
fon = wrap.sprite.add("foi", 500, 400, "fon")
fon = wrap.sprite.set_size(fon, 1000, 800)
ooe = wrap.sprite.add_text(" ", 500, 300, text_color=(0, 255, 4), font_size=50)
baraban_on = 0
spisok_id_zhifr = []
zifre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kolvomonet = 10
vipavshee_chislo=None
wrap.sprite.add_text("МОНЕТЫ", 80, 25, text_color=(0, 255, 4), font_size=30)
kolvomonet_id = wrap.sprite.add_text(str(kolvomonet), 180, 25, text_color=(0, 255, 4), font_size=30)


def kazinritapora():
    x = 200

    for did in zifre:
        x += 50
        if did == 10:
            x += 20
        id_sprite = wrap.sprite.add_text(str(did), x, 650, text_color=(0, 123, 4), font_size=50,
                                         back_color=[255, 12, 0])

        spisok_id_zhifr.append(id_sprite)


@wrap.always()
def vibor_zifor():
    global  vipavshee_chislo
    if baraban_on == 1:
        pervoe = zifre[7]
        vtoroe = zifre[7]

        vipavshee_chislo = random.randint(int(pervoe), int(vtoroe))
        wrap.sprite_text.set_text(ooe, str(vipavshee_chislo))
        print(vipavshee_chislo)

@wrap.on_key_down(wrap.K_SPACE)
def rererererere():
    global baraban_on ,stavka,kolvomonet
    if baraban_on == 0:
        baraban_on = 1
    else:

        baraban_on = 0
        stavka=wrap.sprite_text.get_text(stavka)
        stavka=int(stavka)
        if vipavshee_chislo==stavka :
            kolvomonet += 5
            wrap.sprite_text.set_text(kolvomonet_id, str(kolvomonet))


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def delaem_stavku(pos_x, pos_y):
    global old, vipavshee_chislo, kolvomonet,stavka
    for did in spisok_id_zhifr:

        yre = wrap.sprite.is_collide_point(did, pos_x, pos_y)

        if yre == True:
            stavka = did
            wrap.sprite_text.set_text_color(old, 0, 123, 4)

            wrap.sprite_text.set_text_color(did, 0, 0, 255)
            old = did







kazinritapora()
old = spisok_id_zhifr[0]
wrap.sprite_text.set_text_color(old, 0, 0, 255)

import wrap_py

wrap_py.app.start()
