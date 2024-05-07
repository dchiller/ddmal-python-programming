def check_types_add_numbers(
        *args):
    for arg in args:
        if not isinstance(arg, (int, float)):

            
            raise TypeError("Only numbers are allowed")
    return sum(args)
