try:
    from foo import bar
except ImportError:

    def bar():
        raise NotImplementedError
