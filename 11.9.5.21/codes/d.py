import numpy as np
import matplotlib.pyplot as plt

def plot_data(file_name, title, ylabel):
    # Read data from the text file
    with open(file_name, "r") as file:
        data = [line.strip().split() for line in file]

    # Separate values of n and x(n)
    n_values, x_values = zip(*[(int(line[0]), float(line[1])) for line in data])

    # Plot the stem graph without grid
    plt.stem(n_values, x_values, basefmt='b-', linefmt='r-', markerfmt='ro')
    plt.title(title)
    plt.xlabel('n')
    plt.ylabel(ylabel)
    plt.grid(False)  # Remove the grid
    plt.savefig(f'{file_name.split(".")[0]}.png', dpi=300, bbox_inches='tight')
    plt.show()
def main():
    plot_data("data_x1.txt", "", '$s_1(n)$')
    plot_data("data_x2.txt", "", '$s_2(n)$')

if __name__ == "__main__":
    main()

