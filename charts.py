import matplotlib.pyplot as plt


def show_chart(values):

    days = range(len(values))


    plt.plot(days, values)

    plt.title("Portfolio evolution")

    plt.xlabel("Days")

    plt.ylabel("Value ($)")


    plt.show()
