import ast


class Context(list):
    allow_bare_raise = True


class RaiseStatementChecker:
    name = "flake8-raise"
    version = "0.0.4"
    text = {
        "R100": "R100 raise in except handler without from",
        "R101": "R101 use bare raise in except handler",
    }

    def __init__(self, tree, filename):
        self.tree = tree
        self.handlers = [Context()]

    def run(self):
        yield from self.walk(self.tree)

    def walk(self, node):
        if isinstance(node, ast.FunctionDef):
            self.handlers.append(Context())
        elif isinstance(node, ast.ExceptHandler):
            self.handlers[-1].allow_bare_raise = True
            self.handlers[-1].append(node.name)
        elif isinstance(node, ast.Raise):
            if self.handlers[-1] and node.exc is not None:
                if node.cause is None and not (
                    isinstance(node.exc, ast.Name) and node.exc.id in self.handlers[-1]
                ):
                    yield node.lineno, node.col_offset, self.text["R100"], type(self)

                if (
                    self.handlers[-1].allow_bare_raise
                    and isinstance(node.exc, ast.Name)
                    and node.exc.id == self.handlers[-1][-1]
                ):
                    yield node.lineno, node.col_offset, self.text["R101"], type(self)

        for child in ast.iter_child_nodes(node):
            yield from self.walk(child)

        if isinstance(node, ast.FunctionDef):
            del self.handlers[-1]
        elif isinstance(node, ast.ExceptHandler):
            self.handlers[-1].allow_bare_raise = False
            del self.handlers[-1][-1]
