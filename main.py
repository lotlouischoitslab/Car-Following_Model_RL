from src.utils import Vehicle

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Instantiate a Vehicle
    vehicle = Vehicle(v_max=33.3, a=0.3, b=3, T=1.5, s_0=2, delta=4)

    # Time step
    dt = 0.1

    # Initialize speeds and distances
    v_front = 20
    s_front = 100

    # Lists to store speed and position over time
    time = []
    speed = []
    position = []

    # Simulation for 100 time steps
    for t in range(100):
        v, s = vehicle.update(v_front, s_front, dt)
        time.append(t*dt)
        speed.append(v)
        position.append(s)

    # Plot speed and position over time
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Speed (m/s)', color=color)
    ax1.plot(time, speed, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Position (m)', color=color)
    ax2.plot(time, position, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()

if __name__ =='__main__':
    main()