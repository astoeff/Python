from choose import (
choose_random_spell_from_file,
choose_random_weapon_from_file,
choose_random_treasure_from_file
)


class Dungeon:
    def __init__(self, file):
        self.list_map = [[]]
        self.map = self.to_string(file=file)
        self.validate_map()
        self.to_list()
        self.treasures_file = file.replace('.txt', '_treasures.txt')


    @classmethod
    def from_string(cls, string):
        with open("test.txt", 'w') as f:
            f.write(string)
        return cls(file="test.txt")


    def to_string(self, file=None, list=None):
        if file:
            with open(file, 'r') as f:
                return f.read()
        elif list:
            return "\n".join(["".join(lst) for lst in list])
        else:
            raise ValueError


    def validate_map(self):
        assert 'S' in self.map, "No starting point"

        gates = 0
        for symbol in self.map:
            if symbol == "G":
                gates += 1
        assert gates == 1, "Number of gates != 1"


    def print_map(self):
        print(self.map)


    def spawn(self, hero):
        if 'H' in self.map:
            return False
        if 'S' in self.map:
            self. map = self.map.replace('S', 'H', 1)
            return True
        else:
            return False


    def move_hero(self, direction):
        current_position = self.map.replace('\n', '').index('H')
        current_x = current_position % len(self.list_map[0])
        current_y = current_position // len(self.list_map[0])
        new_x = current_x
        new_y = current_y

        if direction == 'right':
            new_x = current_x + 1
        elif direction == 'left':
            new_x = current_x - 1
            if new_x < 0:
                return False
        elif direction == 'up':
            new_y = current_y - 1
            if new_y < 0:
                return False
        elif direction == 'down':
            new_y = current_y + 1
        else:
            return False

        try:
            if self.list_map[new_y][new_x] == '#':
                return False
            elif self.list_map[new_y][new_x] == 'T':
                treasure = self.pick_treasure()
                print("Found treasure!")
        except IndexError:
            return False
        else:
            self.list_map[current_y][current_x] = '.'
            self.list_map[new_y][new_x] = 'H'
            self.map = self.to_string(list=self.list_map)
            return True



    def to_list(self):
        i = 0
        for symbol in self.map:
            if symbol == '\n':
                self.list_map.append([])
                i += 1
            else:
                self.list_map[i].append(symbol)
        # with open(file, 'r') as f:
        #     i = 0
        #     for line in f.readlines():
        #         self.map.append([])
        #         for symbol in line:
        #             if symbol != '\n':
        #                 self.map[i].append(symbol)
        #         i += 1


    def pick_treasure(self, string=None):
        return choose_random_treasure_from_file(self.treasures_file)
