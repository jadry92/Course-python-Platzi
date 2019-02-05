import sys
import os
import csv

clients_list = []
CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'number']

def create_client(client_info):
    global clients_list

    clients_list.append(client_info)

def show_clients():
    global clients_list
    for id, client in enumerate(clients_list):
        print(' {uid} | {name} | {company} | {number}'.format(
        uid=id,
        name=client['name'],
        company=client['company'],
        number=client['number']
        ))

def update_client(name):
    global clients_list
    id = _search_index(name)
    flag_update_done = False
    while not flag_update_done:
        _print_comands_update()
        key = _ask_for_data('')
        key = key.upper()
        if key == 'N':
            value = _ask_for_data('What is the client name ?')
            clients_list[id]['name'] = value
        elif key == 'C':
            value = _ask_for_data('Which company is the client working ?')
            clients_list[id]['company'] = value
        elif key == 'E':
            value = _ask_for_data('What is the client email ?')
            clients_list[id]['email'] = value
        elif key == 'C':
            value = _ask_for_data('Which country code is client the phone number?')
            clients_list[id]['email'] = value
        elif key == 'P':
            number_st = _ask_for_data('What is the client phone number ?')
            country_code_st = _ask_for_data('Which country code is client the phone number?')
            clients_list[id]['number'] = '+' + country_code_st + '-' + number_st
        elif key == 'EXIT':
            flag_update_done = True
        else:
            print('Wrong command')

def delete_client(name_del):
    global clients_list
    id = _search_index(name_del)
    if id != None:
        del clients_list[id]

def _search_index(name):
    global clients_list

    for id in range(len(clients_list)):
        if clients_list[id]['name'] == name:
            return id

    print('Error : Name is not in the data base')
    return None

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients_list.append(row)


def _save_clients_to_storage():
    tmp_table_name = CLIENT_TABLE + '.tmp'
    with open(tmp_table_name,mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients_list)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name ,CLIENT_TABLE)

def _print_welcome():
    print('WELCOME TO PLATZI STORE')
    print('*'*50)
    print('What would you like to do today ?')
    _print_main_comands()

def _print_main_comands():
    print('[U]pdate client')
    print('[R]ead client')
    print('[C]reate client')
    print('[D]elete client')
    print('[S]earch client information')
    print('[--help] help')

def _print_comands_update():
    print('Which field would you like to update?')
    print('[N]ame')
    print('[C]company')
    print('[E]mail')
    print('[C]ountry code')
    print('[P]hone number')
    print('[exit]')

def _get_client_information():
    name = _ask_for_data('What is the client name ?')
    company = _ask_for_data('Which company is the client working ?')
    email = _ask_for_data('What is the client email ?')
    number_st = _ask_for_data('What is the client phone number ?')
    country_code_st = _ask_for_data('Which country code is client the phone number?')
    output = {
        'name' : name,
        'company' : company,
        'email' : email,
        'number' : '+' + country_code_st + '-' + number_st # [country code, number]
    }
    return output

def _ask_for_data(question_to_ask):
    output = None
    while  not output :
        output = input(question_to_ask)
        if output == 'exit':
            output = None
            break
    if not output:
        sys.exit()
    return output

def _get_client_name(text = ''):
    output = None
    while  not output :
        if text == '':
            output = input('What is the client name ?')
        else:
            output = input('What is the client name '+text+' ?')
        if output == 'exit':
            output = None
            break
    if not output:
        sys.exit()
    return output

if __name__ == "__main__" :
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()
    #Create client
    if command == 'C':
        client_info = _get_client_information()
        create_client(client_info)
        show_clients()
    # Delete client
    elif command == 'D':
        client_name = _get_client_name('you would like to delete')
        delete_client(client_name)
        show_clients()
    # Update client
    elif command == 'U':
        client_name = _get_client_name('you would like to update')
        update_client(client_name)
        show_clients()
    elif command == 'R':
        show_clients()
    # Help
    elif command == 'S':
        client_name = _get_client_name('you are searching')
        id = _search_index(client_name)
        if id != None:
            print('The name %s excist', client_name)
        else:
            print('The name {} not excist'.format(client_name))
    elif command == '--help':
        _print_commands()
    else:
        print('Invalid Command')
        print('you should use \'--help\' for more information ')

    _save_clients_to_storage()
