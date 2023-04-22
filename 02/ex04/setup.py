from setuptools import setup, find_packages

setup(
    name='my_minipack',
    version='1.0.0',
    description='Howto create a package in python.',
    author='cjung-mo',
    author_email='cjung-mo@student.42.fr',
    url=None,
    license='GPLv3',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Package',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.6',
)
