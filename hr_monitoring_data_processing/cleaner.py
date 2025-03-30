def filter_nondigits(data: list) -> list:
    """
    This function is intended to fliter out raw into a new created list titled "new_list".
    To be specific the function consumes a list of strings and filter out all strings that include non-digit characters.
    Before execution, the function converts the remaining elements and appends it into a "new_list" which will be 
    returned after the function execution.  
    """
    pass
    new_list = []
    for num in data:
        num=num.strip()

        if num.isdigit():
            new_list.append(int(num))
    return new_list