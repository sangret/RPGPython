from random import randint

lista_mobs = []
def criar_mob():
    level = randint(0, 50)
    novo_mob = {
        "name" : f"Monster #{level}",
        "level" : level,
        "damage" : 5 * level,
        "hp" : 100*level 
    }
    lista_mobs.append(novo_mob)
criar_mob()
print(lista_mobs)
