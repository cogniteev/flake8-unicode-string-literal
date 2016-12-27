try:
    import ast
    from ast import iter_child_nodes
except ImportError:
    from flake8.util import ast, iter_child_nodes

__version__ = "1.1"


class UnicodeStringLiteral(object):
    name = "unicode-string-literal"
    version = __version__
    forbidden_str_methods = {'format', }
    W742 = 'W742 Usage of non-unicode string literal: {node.s!r}'
    W743 = u'W743 Unsafe operation on str, should use unicode: {node.s!r}'

    def __init__(self, tree, filename):
        self._node = tree

    @classmethod
    def add_options(cls, parser):
        parser.add_option('--utter-unicode-string-literals',
                          action='store_true',
                          parse_from_config=True,
                          help="Expect all literal strings to be unicode")

    @classmethod
    def parse_options(cls, options):
        cls.all_strings = options.utter_unicode_string_literals

    def run(self):
            return self.visit_tree(self._node) if self._node else ()

    def visit_tree(self, node):
        for error in self.visit_node(node):
            yield error
        for child in iter_child_nodes(node):
            for error in self.visit_tree(child):
                yield error

    def visit_node(self, node):
        if self.all_strings:
            if isinstance(node, ast.Str):
                if not isinstance(node.s, unicode):
                    err = self.W742.format(node=node)
                    yield node.lineno, node.col_offset, err, type(self)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if node.func.attr in self.forbidden_str_methods:
                    if isinstance(node.func.value, ast.Str):
                        if not isinstance(node.func.value.s, unicode):
                            err = self.W743.format(node=node.func.value)
                            yield node.lineno, node.col_offset, err, type(self)
