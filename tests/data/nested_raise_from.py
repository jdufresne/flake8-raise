try:
    pass
except ValueError as e:
    try:
        pass
    except OSError:
        raise TypeError from e
