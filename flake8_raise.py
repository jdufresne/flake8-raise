import ast

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version


class RaiseStatementChecker:
    name = "flake8-raise"
    version = version("flake8-raise")
    text = {
        "R100": "R100 raise in except handler without from",
        "R101": "R101 use bare raise in except handler",
        "R102": "R102 unnecessary parentheses on raised exception",
    }

    def __init__(self, tree, filename):
        self.tree = tree
        self.handlers = [[]]

    def run(self):
        yield from self.walk(self.tree)

    def walk(self, node):
        if isinstance(node, ast.FunctionDef):
            self.handlers.append([])
        elif isinstance(node, ast.ExceptHandler):
            self.handlers[-1].append(node.name)
        elif isinstance(node, ast.Raise):
            if node.exc is not None:
                if self.handlers[-1]:
                    if node.cause is None and not (
                        isinstance(node.exc, ast.Name)
                        and node.exc.id in self.handlers[-1]
                    ):
                        yield node.lineno, node.col_offset, self.text["R100"], type(
                            self
                        )

                    if (
                        isinstance(node.exc, ast.Name)
                        and node.exc.id == self.handlers[-1][-1]
                    ):
                        yield node.lineno, node.col_offset, self.text["R101"], type(
                            self
                        )
                elif (
                    isinstance(node.exc, ast.Call)
                    and not node.exc.args
                    and not node.exc.keywords
                ):
                    yield node.lineno, node.col_offset, self.text["R102"], type(self)

        for child in ast.iter_child_nodes(node):
            yield from self.walk(child)

        if isinstance(node, ast.FunctionDef):
            del self.handlers[-1]
        elif isinstance(node, ast.ExceptHandler):
            del self.handlers[-1][-1]
