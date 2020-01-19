import ast


class RaiseStatementChecker:
    name = "flake8-raise"
    version = "0.0.1"
    text = "R100 raise in except handler without from."

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
            if (
                self.handlers[-1]
                and node.exc is not None
                and node.cause is None
                and not (
                    isinstance(node.exc, ast.Name) and node.exc.id in self.handlers[-1]
                )
            ):
                yield node.lineno, node.col_offset, self.text, type(self)

        for child in ast.iter_child_nodes(node):
            yield from self.walk(child)

        if isinstance(node, ast.FunctionDef):
            del self.handlers[-1]
        elif isinstance(node, ast.ExceptHandler):
            del self.handlers[-1][-1]
