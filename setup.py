from setuptools import setup, find_packages

setup(
    name='terminal-garden',
    version='0.2.0',
    description='A terminal-based virtual plant-growing game.',
    author='Hemanth Gangula',
    author_email='hemanthgangula7@example.com',
    packages=find_packages(include=['terminal_garden', 'terminal_garden.*']),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'terminal-garden=terminal_garden.garden:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)