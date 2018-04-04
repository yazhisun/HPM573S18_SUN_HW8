import Classes as Cls
import scr.FigureSupport as figureLibrary
import SupportTransient as Support

# create a multiple game sets with fair coin
multipleGameSetsFair=Cls.MultipleGameSets(ids=range(1000), prob_head=0.5, n_games_in_a_set=10)
# simulate all game sets
multipleGameSetsFair.simulation()

multipleGameSetsUnfair=Cls.MultipleGameSets(ids=range(1000), prob_head=0.45, n_games_in_a_set=10)
# simulate all game sets
multipleGameSetsUnfair.simulation()

# print outcomes of each cohort
Support.print_outcomes(multipleGameSetsFair, 'With fair coin:')
Support.print_outcomes(multipleGameSetsUnfair, 'When unfair coin:')

# print out comparative outcomes
Support.print_comparative_outcomes(multipleGameSetsFair, multipleGameSetsUnfair)

