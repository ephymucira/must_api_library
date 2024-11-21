from setuptools import setup, find_packages

setup(
    name='mustapi',
    version='0.1.0',
    packages=find_packages(exclude=['tests*', 'examples*']),
    install_requires=[
        'requests>=2.25.0',
        'typing_extensions>=3.7.4'
    ],
    author='Ephy Mucira',
    author_email='ephymucira@gmail.com',
    description='Python client for MustAPI Backend',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mustapi',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov',
            'mypy',
            'black',
            'flake8'
        ]
    }
)