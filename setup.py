from setuptools import setup

with open('unicode_string_literal.py') as istr:
    for line in istr:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip()[1:-1]
            break

setup(
    name='unicode-string-literal',
    description='Flake8 String Literal Enforcer Extension',
    version=version,
    install_requires=[
        'setuptools',
    ],
    author='Cogniteev',
    author_email='tech@cogniteev.com',
    url='https://github.com/cogniteev/flake8-unicode-string-literal.git',
    download_url='https://github.com/cogniteev/flake8-unicode-string-literal/tarball/v' + version,
    zip_safe=False,
    license='Apache license 2.0',
    keywords='flake8 unicode string',
    py_modules=['unicode_string_literal'],
    entry_points={
        'flake8.extension': [
            'W74 = unicode_string_literal:UnicodeStringLiteral',
        ],
    },
)
