from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='mygrader',
    version='0.45a2',
    packages=find_packages(),

    # Add any required dependencies here
    install_requires=['tabulate', 'faker', 'numpy', 'num2words', 'tqdm'],

    author='AppleBoiy',
    author_email='contact.chaipat@gmail.com',
    description='my own CS111 grader.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url="https://github.com/AppleBoiy/my-grader",

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={
        'console_scripts': [
            'your_script=your_package:main',
        ],
    },
    extras_require={
        'tests': [
            'pytest',
            'coverage',
            'pytest-cov'
        ],
    },
)
