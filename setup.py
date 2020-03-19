from setuptools import setup, find_packages

setup(
    name="reading-assistant",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bob-find=assistant.main:main',
        ],
    },
)
