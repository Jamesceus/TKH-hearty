def filter_nondigits(data: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    pass
    new_list = []
    for num in data:
        num=num.strip()

        if num.isdigit():
            new_list.append(int(num))
    return new_list