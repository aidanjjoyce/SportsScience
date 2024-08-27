import matplotlib.pyplot as plt
import numpy as np

def maximum_power(critical_power, anaerobic_work_capacity, max_power, time):
    return (critical_power + (max_power - critical_power) *
            np.tanh(anaerobic_work_capacity / (time * (max_power - critical_power))))

def plot_power_curve(critical_power, anaerobic_work_capacity, max_power):
    times = np.array([t for t in range(5, 60*60, 1)])
    max_powers = maximum_power(critical_power, anaerobic_work_capacity, max_power, times)

    plt.plot(times/60, max_powers)
    plt.ylim(bottom=0, top=1.05 * max_power)
    plt.show()
    return max_powers

if __name__ == "__main__":

    cp = 250
    w = 40000
    mp = 800

    print(plot_power_curve(cp, w, mp))