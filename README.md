# example_package
This repository exists to show a standard python package template
see also [The Hitchikers Guide to Python](https://docs.python-guide.org/writing/structure/).

It is not setup as a template to use with tools such as cookiecutter or copier.

This repository follows the flat layout for simplicity

## There are 2 basic layouts:

Either of these are okay to use, make a decision based on your goals.
See also [The python packaging docs](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)

### Flat layout: the simple approach
This layout may become cluttered with larger projects. A package using 
this layout is importable without installing. For simple packages, and beginner examples, this is fine.

        ├── README.md
        ├── noxfile.py
        ├── pyproject.toml
        ├── setup.py
        ├── awesome_package/
        │   ├── __init__.py
        │   └── module.py
        └── tools/
            ├── generate_awesomeness.py
            └── decrease_world_suck.py        

### SRC layout: the recommended approach
It helps limit issue with implicit import paths, moving the code that's meant to be importable into subdirectories. A package using this kind of layout needs to be installed before importing.

        my_package/
        ├── src/
        │   └── my_package/
        │       ├── __init__.py
        │       ├── module1.py
        │       └── module2.py
        ├── tests/
        │   └── test_module1.py
        ├── pyproject.toml or setup.py
        ├── README.md
        └── LICENSE


## More reading on python packaging and installation

https://packaging.python.org/en/latest/key_projects/



