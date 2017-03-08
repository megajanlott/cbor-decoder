from setuptools import setup, find_packages

setup(
    name='cbor-decoder',
    version='1.0.0.dev1',
    description='A CBOR to JSON and Python decoder',
    long_description='',
    url='https://github.com/megajanlott/cbor-decoder',
    author='megajanlott',
    license='MIT',
    classifiers=[
        # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Interpreters',
    ],
    keywords='cbor json python decoder',
    packages=find_packages(exclude=['docs', 'examples', 'scripts', 'tests']),
    tests_require=['pycodestyle', 'pylint'],
)
