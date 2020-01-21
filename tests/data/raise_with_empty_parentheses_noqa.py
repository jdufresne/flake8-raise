def get_exception_cls():
    return ZeroDivisionError


raise get_exception_cls()  # noqa: R102
