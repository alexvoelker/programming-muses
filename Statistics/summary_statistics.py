import math
from typing import List


class Statistics:
    def __init__(self):
        self.values = []
        self.round_digits = -1

    ''' Handle User Input '''

    def setup_data(self):
        response = input("Enter Sample Data (separated by a space or comma): ").strip()
        data_set = response.split(",") if ',' in response else response.split(' ')
        self.values = sorted([float(value.strip()) for value in data_set])

    def set_values(self, collection: List[float]):
        self.values = sorted(collection)

    def get_values(self):
        return self.values

    def check_empty(self) -> bool:
        return len(self.values) > 0

    def set_round_digits(self, digits: int):
        self.round_digits = digits

    def get_round_digits(self):
        return self.round_digits

    ''' Summary Statistics Functions '''

    def avg(self):
        if not self.check_empty():
            return
        total = sum(self.values)
        return total / len(self.values)

    def median(self):
        return self.median_with_list(self.values)

    def median_with_list(self, collection):
        if len(collection) == 0:
            collection = self.values
        if not self.check_empty():
            return
        return collection[int(len(collection) / 2)] if len(collection) % 2 != 0 else \
            ((collection[int(len(collection) / 2)] + collection[int(len(collection) / 2) - 1]) / 2)

    def std_variance(self):
        """
        :return: A float. Note this function is also called "sample variance"
        """
        if not self.check_empty():
            return
        if len(self.values) == 1:
            return 0
        total = 0
        average = self.avg()
        for x_i in self.values:
            total += (x_i - average) ** 2
        return 1 / (len(self.values) - 1) * total

    def std_deviation(self):
        """
        :return: A float. Note this function is also called "sample standard deviation"
        """
        return math.sqrt(self.std_variance())

    def Q1(self):
        partition = int(len(self.values) / 2)
        return self.median_with_list(self.values[:partition])

    def Q3(self):
        partition = int(len(self.values) / 2)
        if len(self.values) % 2 != 0:
            partition = int(len(self.values) / 2) + 1
        return self.median_with_list(self.values[partition:])

    def IQR(self):
        return self.Q3() - self.Q1()

    def outliers_high(self):
        threshold = self.Q3() + 1.5 * self.IQR()
        outliers = []
        for value in self.values:
            if value > threshold:
                outliers.append(value)
        if len(outliers) == 0:
            return "none"
        return outliers

    def outliers_low(self):
        threshold = self.Q1() - 1.5 * self.IQR()
        outliers = []
        for value in self.values:
            if value < threshold:
                outliers.append(value)
        if len(outliers) == 0:
            return "none"
        return outliers
    ''' Summary Statistics Output '''

    def print_summary_statistics(self):
        if not self.check_empty():
            return
        if self.round_digits > 0:
            print("\tData Set: {values} "
                  "\n\tMean: {avg:.{round_digits}f}"
                  "\n\tMedian: {median}"
                  "\n\tStandard Variance: {std_variance:.{round_digits}f}"
                  "\n\tStandard Deviation: {std_deviation:.{round_digits}f}"
                  "\n\tQ1: {q1:.{round_digits}f}"
                  "\n\tQ3: {q3:.{round_digits}f}"
                  "\n\tIQR: {iqr:.{round_digits}f}"
                  "\n\tLow Outliers: {low_outliers} | Bound: {bound_lower}"
                  "\n\tHigh Outliers: {high_outliers} | Bound: {bound_higher}"
                  .format(values=self.values,
                          avg=self.avg(),
                          median=self.median(),
                          std_variance=self.std_variance(),
                          std_deviation=self.std_deviation(),
                          q1=self.Q1(),
                          q3=self.Q3(),
                          iqr=self.IQR(),
                          low_outliers=self.outliers_low(),
                          high_outliers=self.outliers_high(),
                          bound_lower=self.Q1() - 1.5 * self.IQR(),
                          bound_higher=self.Q3() + 1.5 * self.IQR(),
                          round_digits=self.round_digits))
        else:
            print(f"\tData Set: {self.values} "
                  f"\n\tMean: {self.avg()} "
                  f"\n\tMedian: {self.median()} "
                  f"\n\tStandard Variance: {self.std_variance()} "
                  f"\n\tStandard Deviation: {self.std_deviation()}"
                  f"\n\tQ1: {self.Q1()}"
                  f"\n\tQ3: {self.Q3()}"
                  f"\n\tIQR: {self.IQR()}"
                  f"\n\tLow Outliers: {self.outliers_low()} | Bound: {self.Q1() - 1.5 * self.IQR()}"
                  f"\n\tHigh Outliers: {self.outliers_high()} | Bound: {self.Q3() + 1.5 * self.IQR()}")
