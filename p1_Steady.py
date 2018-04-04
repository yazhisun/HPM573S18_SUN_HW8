import Classes as Cls
import scr.FigureSupport as figureLibrary
import SupportSteady as Support

# Calculate expected reward of 1000 games
fairset = Cls.SetOfGames(id=1, prob_head=0.5, n_games=1000)
fairsetoutcome=fairset.simulation()

unfairset = Cls.SetOfGames(id=2, prob_head=0.45, n_games=1000)
unfairsetoutcome=unfairset.simulation()

Support.print_outcomes(fairsetoutcome, 'With fair coin:')
Support.print_outcomes(unfairsetoutcome, 'With unfair coin:')

Support.print_comparative_outcomes(fairsetoutcome, unfairsetoutcome)
