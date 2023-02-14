from summary_statistics import Statistics

stats = Statistics()
stats.setup_data()
stats.set_round_digits(int(input("Digits to round to? (-1 for non-rounded value): ")))
stats.print_summary_statistics()