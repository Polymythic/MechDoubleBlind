class Mech():
    '''
    Mech class
    '''

    def __init__(self, name, tonnage, starting_map=0, starting_grid=0, starting_facing=0):
        self.name = name
        self.tonnage = tonnage
        self.starting_map = starting_map
        self.starting_grid = starting_grid
        self.starting_facing = starting_facing
        