import numpy as np

from utils.Sorter import Sorter
from utils.Utils import Timer, Logger


def generate_random_arrays(arr_sizes):
    generated_arrays = []
    for arr_size in arr_sizes:
        temp_arr = np.random.randint(MAXIMUM_INTEGER,size=arr_size)
        generated_arrays.append(temp_arr)
        # logger.debug("size={}".format(temp_arr.size))
        # logger.debug(temp_arr)
    return generated_arrays

def sortArray(array, method):
    array_clone = array[:]
    sorted_array = sorter.sort(array_clone, method)
    # logger.debug(sorted_array)

    return sorted_array

def sortEveryArraysWithTimer(every_arrays):
    for array in every_arrays:
        methods = ["quick", "insertion", "combine"]

        elapsed_time = [0,0,0]
        for idx, method in enumerate(methods):
            timer.tic()
            count = 0
            while True:
                sortArray(array, method)
                count += 1
                # logger.debug("count={}, timer.toc()={}".format(count, timer.toc()))
                if (timer.toc() > TOTAL_TIME_IN_SECS):
                    break
            elapsed_time[idx] = round(timer.toc_in_millis() / count, 5)
            logger.info("N={}, method={}, elapsed_time={}ms, count={}".format(
                                array.size, method, elapsed_time[idx], count))

            if not sorter.nbreak_setted and array.size is not 0:
            # nbreak set only one time.
            # no consideration N=0
                if method is "insertion":
                    if elapsed_time[0] < elapsed_time[1]: # quick < insertion
                        logger.info("set nbreak={}".format(
                            array.size))
                        sorter.set_nbreak(array.size)
        if elapsed_time[0] < elapsed_time[1]:
            inequality = "<"
        else:
            inequality = ">"
        logger.info("quick={}ms {} insertion={}ms".format(
            elapsed_time[0], inequality, elapsed_time[1]))


# init Timer
timer = Timer.getInstance()
# logger = Logger.getLogger("DEBUG")
logger = Logger.getLogger("INFO")
sorter = Sorter.getInstance()


# CONSTANTS
MAXIMUM_INTEGER = 60000 # limitation integer 0-60000
TOTAL_TIME_IN_SECS = 1
# TOTAL_TIME_IN_SECS = 100 # for experiments

# init Array sizes
ARR_SIZES  = [size for size in range(   0, 100,  10)]
ARR_SIZES += [size for size in range( 100,1000, 100)]
ARR_SIZES += [size for size in range(1000,5001,1000)]

# generate Array
every_arrays = generate_random_arrays(ARR_SIZES)

# sort
sortEveryArraysWithTimer(every_arrays)
