from src.utils import Vehicle

def main():
    # Instantiate a Vehicle
    vehicle = Vehicle(v_max=33.3, a=0.3, b=3, T=1.5, s_0=2, delta=4)

    # Time step
    dt = 0.1

    # Initialize speeds and distances
    v_front = 20
    s_front = 100

    # Simulation for 100 time steps
    for t in range(1,100):
        v, s = vehicle.update(v_front, s_front, dt)
        print(f"At time {t*dt}: speed = {v}, position = {s}")

if __name__ =='__main__':
    main()