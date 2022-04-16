from strings import FILENAME
from DBClass import DBClass

NOTE_LIST = list()


def write():
    file = open(FILENAME, 'w')
    file.truncate()
    file.close()
    with open(FILENAME, 'w') as file:
        for o in NOTE_LIST:
            file.write(o.write_string() + '\n')


def read():
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.replace('\n', '', 1).split('|')
            NOTE_LIST.append(DBClass(elem_id=len(NOTE_LIST) + 1, version=line[0], places_count=line[1],
                                     data=line[2], name=line[3], price=line[4], service_cost=line[5],
                                     description=line[6], term=line[7]))
