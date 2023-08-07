from setuptools import setup, find_packages

setup(
    name='mygrader',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[],  # Add any required dependencies here
    author='AppleBoiy',
    author_email='contact.chaipat@gmail.com',
    description='my own CS111 grader.',

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
        'test': [
            'pytest',
            'coverage',
            'pytest-cov'
        ],
    },
)

