
clients_list = ['sebas','johan']

def create_client(client_name):
    global clients_list

    clients_list.append(client_name)

def show_clients():
    global clients_list
    print(clients_list)

def update_client(name_old):
    global clients_list
    try:
        id = clients_list.index(name_old)
        name_new = _get_client_name()
        clients_list[id] = name_new
    except:
        print('Error : Name is not in the data base')

def delete_client(name_del):
    global clients_list
    try:
        id = clients_list.index(name_del)
        del clients_list[id]
    except:
        print('Error : Name is not in the data base')


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would you like to do today ?')
    _print_comands()

def _print_comands():
    print('[U]pdate client')
    print('[R]ead client')
    print('[C]reate client')
    print('[D]elete client')
    print('[--help] help')

def _get_client_name(text = ''):
    output = ''
    if text == '':
        output = input('What is the client name ?')
    else:
        output = input('What is the client name '+text+' ?')
    return output

if __name__ == "__main__" :
    _print_welcome()

    command = input()
    command.upper()
    #Create client
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        show_clients()
    # Delete client
    elif command == 'D':
        client_name = _get_client_name('you will delete')
        delete_client(client_name)
        show_clients()
    # Update client
    elif command == 'U':
        client_name = _get_client_name('you will update')
        update_client(client_name)
        show_clients()
    elif command == 'R':
        show_clients()
    # Help
    elif command == '--help':
        _print_commands()
    else:
        print('Invalid Command')
        print('you should use \'--help\' for more information ')
