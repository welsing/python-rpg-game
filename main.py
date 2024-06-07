import random




# CRIA PLAYER
player = {
    "name": input("Whats is your name?: ").strip(),
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,

}


def create_monster(max_level):
    level = random.randint(1,max_level)
    novo_npc = {
        "name": f"Monstro #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level
    }
    return novo_npc


def view_player_stats():
        print(f" - {player["name"]} | LEVEL {player['level']} | HP {player["hp"]} | DAMAGE {player["damage"]}")


def view_npcs_around():
    for npc in npc_monsters:
        print(f" - {npc["name"]} | LEVEL {npc['level']} | HP {npc["hp"]} | DAMAGE {npc["damage"]}")


def generate_monsters(qtd, level_max):
    for qtd in range(qtd):
        npc = create_monster(level_max)
        npc_monsters.append(npc)





# LISTAS PRIMORDIAIS 
npc_monsters = []




generate_monsters(5, 10)
view_npcs_around()
view_player_stats()