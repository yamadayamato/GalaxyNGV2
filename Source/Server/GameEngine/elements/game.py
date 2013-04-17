# vi: spell spl=en

from element.turn  import Turn

class Game(object):

    """Game -- all data for a single game.
    """
    def __init__(self):
        self.name  = None
        self.turn  = []


    """Create a new game
    """
    def create(self, game_options ):
        # Create turn 0
        self.turn[ 0 ] = Turn();
        self.turn[ 0 ].create()
