def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    total = 0 
    count = 0

    for item in data:
        total+=item 
        count+= 1
    if count == 0:
        return[]
    
    average = total/count
    average = round(average, 2)
    return average
    


def maximum(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    """
    #pass
    if not data:
        return []
    maximum = data[0]
    for num in data:
        if num>maximum:
            maximum = num
            #num = round(num,2)
    return maximum 


def variance(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population variance)
    """
    #pass
    if len(data) <2:
        return 0
    
    mean = sum(data)/ len(data)
    total = 0
    for num in data:
        total += (num - mean) **2
    var_calculated = total/len(data)

    return var_calculated


def standard_deviation(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population standard deviation)
    """
    #pass
    if len(data) == 0:
        return []
    mean = sum(data)/len(data)
    total = 0 
    for num in data:
        total+= (num - mean) **2

    variance = total/len(data)
    standard_deviation = variance ** 0.5
    return round(standard_deviation,2)
