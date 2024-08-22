import matplotlib.pyplot as plt
import numpy as np

def maximum_power(critical_power, anaerobic_work_capacity, time):
    return critical_power + anaerobic_work_capacity / time

def plot_power_curve(critical_power, anaerobic_work_capacity):
    times = np.array([t for t in range(5, 60*60, 5)])
    max_powers = maximum_power(critical_power, anaerobic_work_capacity, times)

    plt.plot(times, max_powers)
    plt.show()
    return max_powers

if __name__ == "__main__":

    cp = 250
    w = 40000

    print(plot_power_curve(cp, w))