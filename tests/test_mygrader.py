import importlib


def test_import():
    modules = ['mygrader', 'mygrader.src', 'mygrader.src.y2023', 'mygrader.template']
    passed_modules = []

    for module_name in modules:
        try:
            importlib.import_module(module_name)
            passed_modules.append(module_name)
        except ImportError:
            assert False, f'Failed to import {module_name}'

    assert True
