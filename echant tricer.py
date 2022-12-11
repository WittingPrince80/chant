
from tkinter import *
import random

root=Tk()
root.title("Enchant")
root.geometry("500x500")

enchants = ("mending", "unbreaking", "protection", "blast protection","fire protection",
            "projectile protection", "aqua affinity", "resperation", "swift sneak",
            "soul speed", "depth strider", "frost walker", "feather falling",
            "curse of vanishing", "curse of binding", "power", "punch",
            "infinity", "flame", "sharpness", "knockback", "sweeping edge",
            "fire aspect", "efficency","fortune", "silk touch", "luck of the sea", "lure")

used = (17,18,4,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,4,2,4,1,1)

ench = Label(root)
ench["text"] = "Enchants: mending, unbreaking, protection, blast protection,fire protection,projectile protection, aqua affinity, resperation, swift sneak,soul speed, depth strider, frost walker, feather falling,curse of vanishing, curse of binding, power, punch,infinity, flame, sharpness,knockback, sweeping edge,fire aspect, efficency,fortune, silk touch, luck of the sea, lure "
most_used = max(used)
most_used_index = used.index(most_used)
print(most_used_index)

most_used_enchant = enchants[most_used_index]
print("I used " + str(most_used_enchant)+ " " + str(most_used) +" times")

min_used = min(used)
min_used_index = used.index(min_used)
print(min_used_index)

min_used_enchant = enchants[min_used_index]
print("I used " + str(min_used_enchant)+ " " + str(min_used) +" times" )
ench.place(relx= 0.5,rely = 0.4, anchor = CENTER )