from random import randint
from time import sleep


def create_box(var, str):
    line_length = len(str) + len(var) + 9
    top_bottom_border = '-' * line_length
    print(f"{top_bottom_border}\n- {var} - \"{str}\" -\n{top_bottom_border}  \n")



def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)


# CRIA PLAYER
player = {
    "name": "GERALT",
    "level": 1,
    "exp": 0,
    "exp_max": 35,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,   }


# FUNÇÕES DO MUNDO

def dead_npc(i):
    npcs.pop(i)


def create_npc(name, level):
    #level = randint(1,max_level)
    novo_npc = {
        "name": f"{name} #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 9 * level
    }
    npcs.append(novo_npc)


# def generate_monsters(qtd, level_max):
#     for qtd in range(qtd):
#         npc = create_monster(level_max)
#         npc_monsters.append(npc)

def view_player_stats():
        print(f" - {player["name"]} | LEVEL {player['level']} | HP {player["hp"]} | DAMAGE {player["damage"]} | EXP {player['exp']}/{player['exp_max']}")


def view_npcs_around():
    for npc in npcs:
        print(f" - {npc["name"]} | LEVEL {npc['level']} | HP {npc["hp"]} | DAMAGE {npc["damage"]} | EXP.: {npc["exp"]}")





def battle_specs():
    print(f"{player['name']}: {player['hp']}/{player['hp_max']}  || {npc_selecionado['name']}: {npc_selecionado['hp']}/{npc_selecionado['hp_max']}")

# AÇÕES

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['hp_max'] += 20
        reset_player()
        print("--- LEVEL UP!! ---")


def reset_player():
    player['hp'] = player['hp_max']

def who_wins(npc):
    return player['hp'] <= 0  or npc['hp'] <= 0

def start_battle(npc):
    while True:
        if who_wins(npc):

            if npc['hp'] <= 0:
                player['exp'] += npc['exp']
                dead_npc(npcs.index(npc))
                level_up()
                print(f"{player['name']} VENCEU A BATALHA!")
                view_player_stats()

            else:
                print(f"{npc['name']} DERROTOU {player['name']}!")
            sleep(4)
            clear()
            break

        attack_npc(npc)
        sleep(1)
        attack_player(npc)
        sleep(1)
        
        
        battle_specs()



def attack_npc(npc):
    npc['hp'] -= player['damage']
    create_box("", f"{player['name']} ATACA {npc['name']} \nDANO CAUSADO: {player['damage']} ")


def attack_player(npc):
    player['hp'] -= npc['damage']
    create_box("", f"{npc['name']} ATACA {player['name']} \nDANO CAUSADO: {npc['damage']} ")



def escolha(esc1, esc2):
    esc = input("DIGITE: ")
    return esc


# LISTAS PRIMORDIAIS 
npcs = []


while True:
    print("INICIANDO GAME...")
    sleep(2)
    clear()
    create_box(player['name'], "Oi, onde eu estou? parece que apaguei")

    create_npc("Vesemir", 20)
    npc_selecionado = npcs[0]
    create_box(npc_selecionado["name"], "Epa doidão, tu ficou muito louco FISSTECH")


    create_box("ESCOLHA:", "DESEJA BATALHAR CONTRA VESEMIR? [S/N]")
    sorn = input("DIGITE: ").strip().lower()
    if sorn == 's':
        view_npcs_around()
        start_battle(npc_selecionado)
        break

    sleep(1)
    clear()

    create_box("NARRADOR: ", "Após algumas horas, Vesemir tinha explicado a Geralt toda a confusão\n Após Yennefer enganar geralt em uma partida de GWENT, ele bebeu vinho batizado.")
    sleep(2)
    create_box(npc_selecionado["name"], "Então, foi assim que você veio parar aqui no hospicio de Velen...")
    sleep(2)


    create_box("ESCOLHA: ", "[1] - Mas onde foi parar minhas espadas? \n [2] Entendo, nossa mas agora o que cairia bem seria um cerveja ")
    sleep(2)
    sorn = input("DIGITE: ").strip()
    if sorn == "1":
        create_box(npc_selecionado["name"], "Bom amigo, elas foram perdidas, e por isso vim aqui. \n Nenhum bruxo pode ficar sem sua espada.")
        sleep(2)
    else:
        create_box(npc_selecionado["name"], "Que cervaja GERALT! Devemos focar no por que estou aqui.")
        sleep(2)
        create_box("ESCOLHA: ", "[1] - E por que está aqui?? \n [2] Não, somente depois de um drink. ")
        sleep(2)
        sorn = input("DIGITE: ").strip()
        if sorn == "1":
            create_box(npc_selecionado["name"], "Você perdeu suas espadas depois das palhaçadas de Yen.")
            sleep(2)
        else:
            create_box(npc_selecionado["name"], "Beleza, mas na sua conta.")
            sleep(2)

    create_box("NARRADOR: ", "Geralt e Vesemir sairam a busca das espadas, contudo, se esbarram com problemas.")
    sleep(2)
    create_npc("SOLDADO NILF", 2)
    create_box("SOLDADO NILFGARDIANO", "Ei, aberração, espero que você não esteja criando problemas.")
    sleep(2)
    create_box(player['name'], "Vai toma no cu!")
    sleep(4)
    clear()
    npc_selecionado = npcs[1]
    start_battle(npc_selecionado)




    break


print("--- GAMEOVER ----")















# generate_monsters(5, 1)
view_npcs_around()
# npc_selecionado = npc_monsters[int(input("QUAL NPC DESEJA ATACAR?: "))]
# start_battle(npc_selecionado)

# view_npcs_around()
# npc_selecionado = npc_monsters[int(input("QUAL NPC DESEJA ATACAR?: "))]
# start_battle(npc_selecionado)

# view_npcs_around()
# npc_selecionado = npc_monsters[int(input("QUAL NPC DESEJA ATACAR?: "))]
# start_battle(npc_selecionado)

# view_npcs_around()
# npc_selecionado = npc_monsters[int(input("QUAL NPC DESEJA ATACAR?: "))]
# start_battle(npc_selecionado)

    
# view_npcs_around()
# npc_selecionado = npc_monsters[int(input("QUAL NPC DESEJA ATACAR?: "))]
# start_battle(npc_selecionado)

    
#view_player_stats()



