#!/usr/bin/env python
import matplotlib.pyplot as plt


class ComparisonPlotter:
    def __init__(self, data_list):
        self.trajectory_fig, self.trajectory_plot = plt.subplots(1, 1)
        self.position_fig, self.position_plot = plt.subplots(2, 1, sharex=True)
        self.position_error_fig, self.position_error_plot = plt.subplots(2, 1, sharex=True)
        self.control_action_fig, self.control_action_plot = plt.subplots(2, 1, sharex=True)

    def plot_comparison(self):
        plt.show()

if __name__ == '__main__':
    ComparisonPlotter([]).plot_comparison()
