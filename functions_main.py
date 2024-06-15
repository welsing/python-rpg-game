from random import randint


# CRIA PLAYER
player = {
    "name": input("Whats is your name?: ").strip(),
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,   }


# FUNÇÕES DO MUNDO

def create_monster(max_level):
    level = randint(1,max_level)
    novo_npc = {
        "name": f"Monstro #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level
    }
    return novo_npc


def view_player_stats():
        print(f" - {player["name"]} | LEVEL {player['level']} | HP {player["hp"]} | DAMAGE {player["damage"]}")


def view_npcs_around():
    for npc in npc_monsters:
        print(f" - {npc["name"]} | LEVEL {npc['level']} | HP {npc["hp"]} | DAMAGE {npc["damage"]} | EXP.: {npc["exp"]}")


def generate_monsters(qtd, level_max):
    for qtd in range(qtd):
        npc = create_monster(level_max)
        npc_monsters.append(npc)


def battle_specs():
    print(f"{player['name']}: {player['hp']}/{player['hp_max']}  || {npc_selecionado['name']}: {npc_selecionado['hp']}/{npc_selecionado['hp']}")

# AÇÕES

def start_battle(npc):
    while True:
        if player['hp'] <= 0  or npc_selecionado['hp'] <= 0:
            break
        attack_npc(npc)
        attack_player(npc)
        battle_specs()


def attack_npc(npc):
    npc['hp'] -= player['damage']


def attack_player(npc):
    player['hp'] -= npc['damage']

def select_npc(npc):
    npc_selecionado = npc_monsters[int(input("QUAL NPC DESEJA ATACAR?: "))]

# LISTAS PRIMORDIAIS 
npc_monsters = []