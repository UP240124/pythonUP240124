#1
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choices(characters, k=6))
print(random_user_id())

#2
ID= int(input( "number of IDs "))
digits= int(input("number of characters:  "))
def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    IDS = [''.join(random.choices(characters, k=digits)) for _ in range(ID)]
    return IDS
generated_ids = user_id_gen_by_user()
for gen in generated_ids:
    print(gen)

#33
def rgb_color_gen ():
    random.randint(0,10)
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    print(f"rgb({r}, {g}, {b})")
print(rgb_color_gen())