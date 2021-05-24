import re


def f21(mas):
    if mas[1] == 1967:
        if mas[2] == 'yaml':
            return 9
        elif mas[2] == 'eq':
            if mas[3] == 'urweb':
                return 6
            elif mas[3] == 'dm':
                return 7
            elif mas[3] == 'mirah':
                return 8

    elif mas[1] == 2015:
        if mas[2] == 'eq':
            if mas[0] == 'ats':
                return 0
            elif mas[0] == 'wisp':
                return 1
            elif mas[0] == 'ston':
                return 2
        elif mas[2] == 'yaml':
            if mas[0] == 'ats':
                return 3
            elif mas[0] == 'wisp':
                return 4
            elif mas[0] == 'ston':
                return 5