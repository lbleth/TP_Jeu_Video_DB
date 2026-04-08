from pymongo import MongoClient
import random
import os
import time
import db_init
import utils

def team_is_alive(team):
    for character in team:
        if is_alive(character):
            return True
    return False

def is_alive(character):
    return character['hp'] > 0

def start_fight(team):
    wave = 1
    utils.center("DEBUT DU COMBAT")
    enemy = utils.choose_enemy()
    while team_is_alive(team):
        utils.center(f"VAGUE {wave}")
        while is_alive(enemy) and team_is_alive(team):
            attack_enemy(team, enemy)
            if is_alive(enemy):
                attack_ally(enemy, team)
        if team_is_alive(team) and not is_alive(enemy):
            wave += 1
            print("Un ennemi arrive...")
            enemy = utils.choose_enemy()
    print("Perdu ! Partie terminée.")
    utils.center(f"Vous avez survécu {wave - 1} manches")
    player_name = utils.username()
    return player_name

def attack_enemy(team, enemy):
    for character in team:
        if is_alive(character):
            damage = received_damage(character, enemy)
            enemy['hp'] -= damage
            if enemy['hp'] < 0:
                enemy['hp'] = 0
            print(f"{character['name']} attaque {enemy['name']} et inflige {damage} dégâts.")
            if not is_alive(enemy):
                print(f"{enemy['name']} a été battu.")
                break
            time.sleep(0.5)

def attack_ally(enemy,team):
    alive_team = []
    for character in team:
        if is_alive(character):
            alive_team.append(character)
    chosen_char = random.choice(alive_team)
    damage = inflicted_damage(enemy, chosen_char)
    chosen_char['hp'] -= damage
    if chosen_char['hp'] < 0:
        chosen_char['hp'] = 0
    print(f"{enemy['name']} attaque {chosen_char['name']} et inflige {damage} dégâts.")
    if not is_alive(chosen_char):
        print(f"{chosen_char['name']} est mort au combat.")
    time.sleep(0.5)

def received_damage(character, enemy):
    damage = character['atk'] - enemy['def']
    if damage < 0:
        damage = 0 
    return damage

def inflicted_damage(enemy, character):
    dmg_enemy = enemy['atk'] - character['def']
    if dmg_enemy < 0:
        dmg_enemy = 0 
    return dmg_enemy
