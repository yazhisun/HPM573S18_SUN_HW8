import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_gamesets, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of total reward
    survival_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_gamesets.get_mean_total_reward(),
        interval=multi_gamesets.get_PI_total_reward(0.05),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of total reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          survival_mean_PI_text)


def draw_histograms(multigamesetsfair, multigamesetsunfair):
    """ draws the histograms of average survival time
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # histograms of average survival times
    totalreward = [
        multigamesetsfair.get_all_total_rewards(),
        multigamesetsunfair.get_all_total_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets= totalreward,
        title='Histogram of total reward',
        x_label='Reward',
        y_label='Counts',
        bin_width=50,
        legend=['Fair coin', 'Unfair coin'],
        transparency=0.5,
    )


def print_comparative_outcomes(multigamesetsfair, multigamesetsunfair):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean survival time',
        x=multigamesetsunfair.get_all_total_rewards(),
        y_ref=multigamesetsfair.get_all_total_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in average reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
