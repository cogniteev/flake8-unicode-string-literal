# Flake8 String Literal Enforcer Extension

This Python module provide [Flake8](http://flake8.readthedocs.org/)
with an extension that hunt down operations on string literal that may
fail because there are not unicode strings.

# Installation

```shell
pip install unicode-string-literal
```

# Usage

There is nothing to do to take benefits of this extension once it
has been installed. Flake8 will detect it automatically.

# Raised errors

A W742 warning will be issued for any operation made on a non string literal.


For instance:

```python
>>> "this will fail: {}".format(u'€')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\u20ac' in position 0: ordinal not in range(128)
>>>
```

This error will now be prevented with this extension:
```shell
$ cat << EOF | flake8 -
"this will fail: {}".format(u'€')
EOF
stdin:1:1: W743 Unsafe operation on str, should use unicode: 'this will fail: {}'
$
```

# Available options

if the `--utter-unicode-string-literals` option is passed to `flake8` command,
then all `str` string literals will raise an error.

# Issues

Pull-requests are welcome. You can also submit your issues to the
[issues tracker](https://github.com/cogniteev/flake8-unicode-string-literal/issues)

# License

This Flake8 extension is licensed under the Apache License, Version 2.0.
See [LICENSE](LICENSE) file for full license text.
