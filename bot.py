import mouse
import keyboard as kbd


class Mat:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


items = {
    "Wyrdwood Planks" : {
        "ingredients" : {
            "Wyrdwood"  :6,
            "Lumber"    :2,
            "Sandpaper" :1
        }
    },
    "Lumber" : {
        "ingredients" : {
            "Aged Wood" :4,
            "Timber"    :2,
            "Sandpaper" :1
        }
    },
    "Timber" : {
        "ingredients" : {
            "Green Wood" :4
        }
    }
}

shoplist = {}


looking_for = input()
amount = int(input())

def make_list(looking_for, amount, items):
    try:
        item = items.get(looking_for)
        ingredients = item.get("ingredients")
        for key in ingredients.keys():
            shoplist.update({key: ingredients.get(key) * amount})
            make_list(key, ingredients.get(key) * amount, items)
    except:
        try:
            old_amount = shoplist.get(looking_for)
            new_amount = old_amount + amount
            shoplist[looking_for] = new_amount
        except:
            shoplist.update({looking_for: amount})
    return shoplist

shoplist = make_list(looking_for, amount, items)
print(shoplist)










# def test():
#     mouse.move(2067, 48, absolute=True, duration=0.1)
#     mouse.click('left')
#     string = "some text"
#     kbd.write(string, 0.1)



