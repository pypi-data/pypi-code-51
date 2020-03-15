import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import seaborn as sns


class Univariate:
    """

    Useful Resources:
    https://www.arpm.co/symmys-articles/Risk%20and%20Asset%20Allocation%20-%20Springer%20Quantitative%20Finance%20-%20Statistics.pdf
    https://learn.stleonards.vic.edu.au/vcefurthermaths/files/2012/07/Univariate-Statistics-Summary.pdf
    https://psych.unl.edu/psycrs/350/unit2/univ.pdf
    https://www3.nd.edu/~rwilliam/stats1/x03.pdf
    https://www.andrews.edu/~calkins/math/webtexts/statall.pdf

    Usage:

    from argali import descriptive_statistics
    x = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 7, 8, 7, 8, 8, 6, 5, 44, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, -1]
    x_summary = descriptive_statistics.Univariate(data=x)
    x_summary.descriptive_summary()

    """

    def __init__(self, data):
        self.data = data

    def mean(self):
        """
        calculates the mean of a single variable
        :return: mean
        """
        mean = sum(self.data) / len(self.data)
        return mean

    def geometric_mean(self):
        product = 1
        for x in self.data:
            product = product * x

        geometric_mean = product ** (1 / len(self.data))

        return geometric_mean

    def harmonic_mean(self):
        reciprocal = []
        for i in self.data:
            reciprocal.append(i ** -1)
        harmonic_mean = sum(reciprocal) / len(reciprocal)

        return harmonic_mean

    def quadratic_mean(self):
        squared = []
        for i in self.data:
            squared.append(i ** 2)
        quadratic_mean = ((1 / len(squared)) * sum(squared)) ** 0.5
        return quadratic_mean

    def trimmed_mean_01(self):

        trim_index = round(len(self.data) / 100)

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_05(self):

        trim_index = round(len(self.data) / 100) * 5

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_10(self):

        trim_index = round(len(self.data) / 100) * 10

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_custom(self, trim_percentage):

        trim_index = round(len(self.data) / 100) * trim_percentage

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def median(self):
        sorted_ = sorted(self.data)
        if len(sorted_) % 2 == 0:
            median_index = (len(sorted_) / 2) - 1
            median = sorted_[int(median_index)]
        else:
            median_index_top = round(len(sorted_) / 2)
            median_index_bottom = round(len(sorted_) / 2) - 1
            median = (sorted_[median_index_bottom] + sorted_[median_index_top]) / 2

        return median

    def percentile_30(self):
        rank = round(30 / 100 * (len(sorted(self.data))))
        rank += 1
        sorted_ = sorted(self.data)
        rank = sorted_[rank]
        return rank

    def percentile_70(self):
        rank = round(70 / 100 * (len(sorted(self.data))))
        rank += 1
        sorted_ = sorted(self.data)
        rank = sorted_[rank]

        return rank

    def interquartile_range(self):
        iqr = self.percentile_70() - self.percentile_30()
        return iqr

    def unique_value_list(self):
        unique_values = []
        for i in sorted(self.data):
            if i not in unique_values:
                unique_values.append(i)

        return unique_values

    def unique_value_count(self):
        return len(self.unique_value_list())

    def unique_value_frequency(self):
        unique_values = self.unique_value_list()

        value_count_list = []
        for x in unique_values:
            value_count = 0
            for i in sorted(self.data):
                if x == i:
                    value_count += 1
            value_count_list.append(value_count)

        return value_count_list

    def range(self):
        return max(self.data) - min(self.data)

    def deviation_from_mean_list(self):
        mean = self.mean()
        deviation_from_mean_list = []
        for i in sorted(self.data):
            deviation_from_mean_list.append(i - mean)

        return deviation_from_mean_list

    def deviation_squared_list(self):
        deviation_squared = []
        for i in self.deviation_from_mean_list():
            deviation_squared.append(i ** 2)

        return deviation_squared

    def variance(self):
        sum_deviations = sum(self.deviation_squared_list())
        variance = sum_deviations / len(self.deviation_squared_list())

        return variance

    def standard_deviation(self):
        sqrt = self.variance() ** 0.5

        return sqrt

    def skew(self):
        skew = (self.variance() ** 3) / ((len(self.data) * self.standard_deviation()) ** 3)

        return skew

    def kurtosis(self):
        kurtosis = ((self.variance() ** 4) / ((len(self.data) * self.standard_deviation()) ** 4)) - 3

        return kurtosis

    def z_score(self, value):
        z_score = (value - self.mean()) / self.standard_deviation()
        return z_score

    def cumulative_distribution(self):
        cumulative_frequency = []
        cf = 0
        for i in self.unique_value_frequency():
            cf += i
            cumulative_frequency.append(cf)

        fig1 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig1)
        f1_ax1 = fig1.add_subplot(spec2[0, 0])
        plt.plot(cumulative_frequency, marker='o')
        plt.hist(self.data, cumulative=True)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Cumulative Frequency")

        f1_ax2 = fig1.add_subplot(spec2[1, 0])
        sns.kdeplot(self.data)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Kernel Density Estimate")

    def probability_density_function(self):
        sns.set(style="white", palette="muted", color_codes=True)

        f, axes = plt.subplots(2, 2, figsize=(16, 10), sharex=True)
        # sns.despine(left=True)

        # Plot a simple histogram with binsize determined automatically
        sns.distplot(self.data, kde=False, color="b", ax=axes[0, 0])

        # Plot a kernel density estimate and rug plot
        sns.distplot(self.data, hist=False, rug=True, color="r", ax=axes[0, 1])

        # Plot a filled kernel density estimate
        sns.distplot(self.data, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

        # Plot a histogram and kernel density estimate
        sns.distplot(self.data, color="m", ax=axes[1, 1])

        plt.title("Kernel Density Function Plots")
        plt.setp(axes, yticks=[])
        plt.tight_layout()

    def histogram(self):
        """
        Useful Links:
        Plot Documentation - https://matplotlib.org/3.2.0/api/_as_gen/matplotlib.pyplot.hist.html

        :return:
        """
        fig1 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig1)
        f1_ax1 = fig1.add_subplot(spec2[0, 0])
        plt.hist(self.data)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Histogram")

        fi_ax2 = fig1.add_subplot(spec2[1, 1])
        plt.hist(self.data, density=True)
        plt.xlabel('Value')
        plt.ylabel('Normalised Frequency')
        plt.title("Normalised Histogram")

        fig_ax3 = fig1.add_subplot(spec2[0, 1])
        plt.hist(self.data, bins="sqrt")
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Histogram (Bins Determined By SQRT)")

        fig_ax4 = fig1.add_subplot(spec2[1, 0])
        plt.hist(self.data, bins='sturges')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Histogram (Bins Determined By STURGES)")

    def mean_plots(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        means = [self.mean(),
                 self.harmonic_mean(),
                 self.quadratic_mean(),
                 self.geometric_mean(),
                 self.trimmed_mean_01(),
                 self.trimmed_mean_05(),
                 self.trimmed_mean_10()]

        means_plot = plt.bar(x=['Arithmetic',
                                'Harmonic',
                                'Quadratic',
                                'Geometric',
                                'Trimmed Mean 1%',
                                'Trimmed Mean 5%',
                                'Trimmed Mean 10%'], height=means)
        plt.xlabel('Type of Mean')
        plt.ylabel('Value')
        plt.title("Comparison of Means")

        return means_plot

    def mean_vs_median(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        mvm = [self.mean(), self.median()]
        mvm_plot = plt.bar(x=['Mean', 'Mode'], height=mvm)
        plt.ylabel('Value')
        plt.title("Mean Vs Median")

        return mvm_plot

    def violin_plot(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        violin_plot = plt.violinplot(self.data)

        return violin_plot

    def unique_value_distribution(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)

        f2_ax1 = fig2.add_subplot(spec2[0, 0])
        plt.hist(sorted(self.data))
        plt.plot(self.unique_value_list(),
                 self.unique_value_frequency(),
                 label='Occurrence Count', marker='o')
        plt.xlabel('Unique Value')
        plt.ylabel('Frequency')
        plt.title("Unique Value Frequency Distribution")

        f2_ax2 = fig2.add_subplot(spec2[0, 1])
        plt.boxplot(self.data, notch=True, vert=False)
        plt.xlabel('Unique Value')
        plt.title("Box Plot")

        f2_ax3 = fig2.add_subplot(spec2[1, 0])
        num_bins = round(self.unique_value_count() / 3)
        sigma = self.standard_deviation()
        mu = self.mean()
        n, bins, patches = plt.hist(self.data, num_bins, density=1)
        y = ((1 / (((2 * np.pi) ** 0.5) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
        plt.plot(bins, y, '--')
        plt.xlabel('Bin')
        plt.ylabel('Frequency')
        plt.title("Frequency Distribution")

        f2_ax4 = fig2.add_subplot(spec2[1, 1])
        plt.plot(self.deviation_squared_list())
        plt.xlabel('Unique Value')
        plt.ylabel('Squared Difference')
        plt.title("Squared Difference Plot")

        return fig2

    def descriptive_summary(self):
        '''
        Arithmetic Mean Interpretation
        https://en.wikipedia.org/wiki/Arithmetic_mean#Motivating_properties

        Geometric Mean Interpretation
        https://en.wikipedia.org/wiki/Geometric_mean

        Quadratic Mean (RSM)
        http://www.analytictech.com/mb313/rootmean.htm

        Median, Mode
        http://davidmlane.com/hyperstat/desc_univ.html

        Percentiles
        http://onlinestatbook.com/chapter1/percentiles.html
        http://davidmlane.com/hyperstat/desc_univ.html

        Interquartile Range
        http://davidmlane.com/hyperstat/desc_univ.html

        Skew & Kurtosis
        http://davidmlane.com/hyperstat/desc_univ.html

        :return:

        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 4, 5, 6, 5, 6, 5, 6, 3, 8, 5, 4, 3, 9, 10]
        x_summary = Univariate(data=x)
        x_summary.descriptive_summary()
        '''
        print("----------------- \n Descriptive Summary \n -----------------")
        self.mean_plots()
        print("Arithmetic Mean: ")
        print("The mean is the only single number for which the residuals (deviations from the estimate) sum to "
              "zero. If it is required to use a single number as a typical value for a set of known numbers. The "
              "arithmetic mean of this variable is: ", round(self.mean(), 3))

        print("\nGeometric Mean: \n  indicates the central tendency or typical value of a set of numbers by using the "
              "product of their values. The geometric mean applies only to positive numbers. the geometric mean is "
              "only correct mean when averaging normalized results; that is, results that are presented as ratios to "
              "reference values. The geometric mean of this variable is: ", self.geometric_mean())

        print("\nHarmonic Mean: \n The harmonic mean can be expressed as the reciprocal of the arithmetic mean of "
              "the reciprocals of the given set of observations. For all positive data sets containing at least one "
              "pair of nonequal values, the harmonic mean is always the least of the three means,[1] while the "
              "arithmetic mean is always the greatest of the three and the geometric mean is always in between. Since "
              "the harmonic mean of a list of numbers tends strongly toward the least elements of the list, "
              "it tends (compared to the arithmetic mean) to mitigate the impact of large outliers and aggravate the "
              "impact of small ones. The harmonic mean of this variable is: ", self.harmonic_mean())

        print("\nQuadratic Mean:  \n the square root of the mean of the squares of the numbers in the set. The root "
              "mean square is a measure of the magnitude of a set of numbers. It gives a sense for the typical size "
              "of the numbers. The quadratic mean of this variable is: ", self.quadratic_mean())

        print("\nA trimmed mean is less susceptible to the effects of extreme scores than is the arithmetic mean. It "
              "is therefore less susceptible to sampling fluctuation than the mean for extremely skewed distributions. "
              "It is less efficient than the mean for normal distributions.")

        print("\nTrimmed Mean (+- 1%): ", self.trimmed_mean_01())
        print("Trimmed Mean (+- 5%): ", self.trimmed_mean_05())
        print("Trimmed Mean (+- 10%): ", self.trimmed_mean_10())

        print("\nMedian: \n The median is less sensitive to extreme scores than the mean and this makes it a better "
              "measure than the mean for highly skewed distributions. ", self.median())

        print("Mean, Median & Mode Comparison \n The mean, median, and mode are equal in symmetric distributions. The "
              "mean is typically higher than the median in positively skewed distributions and lower than the median "
              "in negatively skewed distributions.")

        self.mean_vs_median()
        plt.show()

        print("\nSkew: \nA distribution is skewed if one of its tails is longer than the other. The skew of the "
              "variable is: ", self.skew())
        print("\nKurtosis: \nKurtosis is based on the size of a distribution's tails. Distributions with relatively "
              "large tails are called leptokurtic; those with small tails are called platykurtic. A distribution with "
              "the same kurtosis as the normal distribution is called mesokurtic. Variable kurtosis is: ",
              self.kurtosis())

        print("Frequency\nNumber of Unique Values: ", self.unique_value_count(), "\n")

        print("The cumulative frequency distribution and related kernel density estimate is shown below:")
        self.cumulative_distribution()
        plt.show()

        print("\nThe variance is computed as the average squared deviation of each number from its mean. The variance "
              "for this variable is: ", self.variance())
        self.probability_density_function()
        plt.show()

        print("A range of histograms with different bin calculations can be found below:")
        self.histogram()
        plt.show()

        print("\nRange: The range is the simplest measure of spread or dispersion: It is equal to the difference "
              "between the largest and the smallest values. The range of this variable is: ", self.range())

        print("\nThe value at the 30th percentile is: ", self.percentile_30())
        print("The value at the 70th percentile is: ", self.percentile_70())
        print("The interquartile range is ", self.interquartile_range())

        print("\nThe standard deviation is the square root of the variance. This variable has a standard deviation of ",
              self.standard_deviation())

        print(
            "The below grid of plots includes additional frequency distributions based on unique values, a box plot and a squared difference plot ")

        self.unique_value_distribution()
        plt.show()
        self.violin_plot()
        print("-----------------")


class Bivariate:
    def __init__(self, variable_1, variable_2):
        self.data_1 = variable_1
        self.data_2 = variable_2

    def comparison_mean(self):
        pass

    def comparison_median(self):
        pass

    def comparison_distribution(self):
        pass

    def comparison_box_plot(self):
        pass


class Multivariate:
    pass
