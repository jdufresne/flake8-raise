try:
    pass
except ValueError as e:
    try:
        pass
    except TypeError:
        pass
    raise e
