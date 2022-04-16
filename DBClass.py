from strings import *


class DBClass:
    def __init__(self, elem_id, version, places_count, data, name, price, service_cost, description, term):
        self.elem_id = elem_id
        self.version = version
        self.places_count = places_count
        self.data = data
        self.name = name
        self.price = price
        self.service_cost = service_cost
        self.description = description
        self.term = term

    def get_id(self):
        return self.elem_id

    def get_list(self):
        return [self.elem_id, self.version, self.places_count, self.data, self.name, self.price,
                self.service_cost, self.description, self.term]

    def write_string(self):
        my_list = [self.version, self.places_count, self.data, self.name, self.price,
                   self.service_cost, self.description, self.term]

        new_string = ''
        for n in my_list:
            new_string += WRITE_STRING_FORMAT % n

        return new_string

    def get_full_string(self):
        my_list = [self.elem_id, self.version, self.places_count, self.data, self.name, self.price,
                   self.service_cost, self.description, self.term]

        new_string = '  '
        for n in my_list:
            new_string += SHOW_STRING_FORMAT % n

        return new_string

    def show_string(self):
        my_list = [self.elem_id, self.version, self.data, self.name]
        new_string = '  '
        for n in my_list:
            new_string += SHOW_STRING_FORMAT % n

        return new_string
