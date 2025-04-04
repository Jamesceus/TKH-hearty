"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    file = open (filename)
    for line in file:
        data.append(line)
    file.close()
    #...

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    filteredData= filter_nondigits(data)
    #...

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    plt.plot(filteredData)
    plt.xlabel ("Time of day")
    plt.ylabel("Heart Rate Data")
    plt.title("HeartyVibes")

    plt.savefig("images/plot.png")
    plt.close()
    #...

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(filteredData)
    max_hr = maximum(filteredData)
    std_dev_hr = standard_deviation(filteredData)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
    #print(run("data/phase1.txt"))
    #print(run("data/phase2.txt"))
    #print(run("data/phase3.txt"))
