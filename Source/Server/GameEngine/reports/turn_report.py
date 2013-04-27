#!/usr/bin/python -3
# vi: spell spl=en

import itertools

from reports.planet_report import PlanetReport
from reports.nation_report import NationReport


class TurnReport(object):

    """A collection of information about the current state of
    the turn from the perspective of a nations.

    Is a subset of all information on the planets, groups,
    nations etc, but with some parts removed or partially removed
    because they were not visible to the nation.

    Information is this report is send to the client.
    """
    def __init__( self, nation, turn_number ):
        self.nation = nation
        self.turn_number = turn_number
        self.planets = []
        # self.battles
        self.nations = []
        # self.messages

    def gather( self, a_turn ):
        """Gather all information for the perspective of the
        nation for which this report is.
        """
        for a_nation in a_turn.all_nations():
            a_nation_report = NationReport( a_nation, a_turn )
            self.nations.append( a_nation_report )

        for a_planet in a_turn.universe.planets.itervalues():
            a_planet_report = PlanetReport( a_turn, self.nation, a_planet )
            self.planets.append( a_planet_report )

        # Handy to have them sorted, makes reports more readable.
        self.planets = sorted( self.planets, key=lambda x : '{:>30}'.format( x.name ) )


    def report_in_text( self, report_file ):
        """Create a plain text turn report from all
        the information in this report.
        """
        report_file.write( 'Nations\n' )
        for i in self.nations:
            report_file.write( "{0} {1} {2} {3} {4} {5} {6}\n".format(
                i.name, i.population, i.industry,
                i.drive_tech, i.weapons_tech,
                i.shield_tech, i.cargo_tech ) )
        report_file.write( '\n' )
        report_file.write( 'Unoccupied Planets\n' )
        report_file.write( 'name,x,y,size,resources\n' )
        for i in itertools.ifilter( lambda p: p.owner == 'Unoccupied', self.planets ):
            report_file.write( "{0:<4} {1:4} {2:4} {3} {4}\n".format( 
                i.name, i.x, i.y, i.size, i.resources ) )
