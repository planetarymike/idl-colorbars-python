import setuptools

setuptools.setup(
    name='idl-colorbars',
    version='1.0',
    description='Load IDL colormaps into matplotlib.',
    url='https://github.com/planetarymike/idl-colorbars-python',
    author=('Mike Chaffin'),
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.10',
        'matplotlib>=3.0.3'],
)
