import copy
import functools
import itertools

win_lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Gana el jugador 2
# board = [1,1,2,0,0,2,0,0,2]

# Gana el jugador 1
# board = [1,1,1,0,0,0,0,0,0]

# No gana nadie
# board = [1,2,1,1,2,2,2,1,1]

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

versions = ["v1.0"]

states = {
    "v1.0": board
}


def get_actions(function, args):
    """ Wrapper for inner functions
    param: function: Is the action to realize.
    param: args: Its an iterable object that's contains the data for inner function
    return: the result of execute the inner function
    """
    return function(args)


def get_last_version(args):
    """ Get current version
    param: versions: Is the current version of state
    return: The version in string format
    """
    if args["versions"].__len__ == 0:
        return args["versions"]
    return args["versions"][-1]


def mark_position(args):
    # args['board'].__len__ < args['position'] -> esto pa que no se pase del rango pero no funca
    if args['board'][args['position'] - 1] == 0:
        new_version = 'v' + str(round(float(args['last_version'].replace('v', '')) + 1, 1))
        args['versions'].append(new_version)
        args['board'][args['position'] - 1] = args['player']
        args['states'][new_version] = copy.deepcopy(args['board'])
        get_actions(print_board, {'board': args['board']})
        return [args['states'], args['versions']]
    else:
        print("\nEsa posición ya fue marcada o se pasó del rango, elige una distinta\n")


def print_board(args):
    """ param:
        board: Game Board with data, it's a list of numbers
    return: print the board in console fot the user
    """
    lista = list(grouper(3, args['board']))

    for linea in lista:
        a, b, c = linea
        print('-------------')
        print('| ' + str(a) + ' | ' + str(b) + ' | ' + str(c) + ' |')


def grouper(n, iterable, fillvalue=None):
    """param:
        n: number to group the iterable list
        iterable: an iterable
    return: a new iterable grouped by n"""

    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def can_i_continue(args):
    """
    Can I Continue Playing?
    This method is called when the function 'calculate_winner' returns None
    param:
        args['board']: Game Board with data, it's a list of numbers
    return: If there's not position with 0 value, the game finished with Draw
    """
    return True if 0 in args['board'] else False


def calculate_winner(args):
    """ Calculate Winner
    param:
        board: Game Board with data, it's a list of numbers
        win_lines: Matrix of the win lines for the game
    return: If there's a winner it'll return the number of the winner (1 or 2), or None if not exits
    """

    for item in args['win_lines']:
        a, b, c = item
        if args['board'][a] and args['board'][a] == args['board'][b] and args['board'][a] == args['board'][c]:
            return args['board'][a]

    return None


def init(value):
    global versions
    global states
    if value != 0:
        states, versions = get_actions(mark_position, {'last_version': get_last_version({'versions': versions}),
                                                       'board': states[get_last_version({'versions': versions})],
                                                       'versions': versions,
                                                       'states': states,
                                                       'position': value,
                                                       'player': 1})
        if get_actions(calculate_winner,
                       {'win_lines': win_lines, 'board': states[get_last_version({'versions': versions})]}) is None:
            if get_actions(can_i_continue, {'board': states[get_last_version({'versions': versions})]}):
                p2 = int(input("Jugador 2 (2) ingrese la posicion que desea repintar entre 1 a 9\n"))
                states, versions = get_actions(mark_position, {'last_version': get_last_version({'versions': versions}),
                                                               'board': states[
                                                                   get_last_version({'versions': versions})],
                                                               'versions': versions,
                                                               'states': states,
                                                               'position': p2,
                                                               'player': 2})
                if get_actions(calculate_winner, {'win_lines': win_lines,
                                                  'board': states[get_last_version({'versions': versions})]}) is None:
                    if get_actions(can_i_continue, {'board': states[get_last_version({'versions': versions})]}):
                        p1 = int(input("Jugador 1 (1) ingrese la posicion que desea repintar entre 1 a 9\n"))
                        init(p1)
                    else:
                        print("\nEl juego termino en empate")
                else:
                    print("El ganador es el jugador nro: " + str(get_actions(calculate_winner, {'win_lines': win_lines,
                                                                                                'board': states[
                                                                                                    get_last_version({
                                                                                                        'versions': versions})]})))
            else:
                print("\nEl juego termino en empate")
        else:
            print("El ganador es el jugador nro: " + str(get_actions(calculate_winner, {'win_lines': win_lines,
                                                                                        'board': states[
                                                                                            get_last_version({
                                                                                                'versions': versions})]})))


print_board({'board': board})
p1 = int(input("Jugador 1 (1) ingrese la posicion que desea repintar entre 1 a 9\n"))
init(p1)
# calculateWinner({'board': board, 'win_lines': win_lines})
# print_board({'board': board})
