from setuptools import setup, find_packages


long_description = open('README.md').read()

setup(
    name='pyCTT',
    version='1.0.1',
    license='MIT License',
    url='https://github.com/dpjrodrigues/pyCTT',
    author='Diogo Rodrigues',
    author_email='dpjrodrigues@gmail.com',
    description='Python library to retrieve package information from CTT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pyCTT'],
    zip_safe=True,
    platforms='any',
    install_requires=[
        'aiohttp',
        'lxml'
      ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
