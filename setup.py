#!/usr/bin/env python

# import setuptools

# if __name__ == "__main__":
    # setuptools.setup()

import setuptools

setuptools.setup(
    name='tagsplit',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'tagsplit=tagsplit:main',
        ]
    }
)
