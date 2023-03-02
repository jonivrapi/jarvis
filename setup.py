from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'jarvis',
    version = '0.0.1',
    author = 'Joni Vrapi',
    license = 'MIT',
    description = 'Its Jarvis',
    py_modules = ['jarvis', 'src'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.10',
    entry_points = '''
        [console_scripts]
        jarvis=jarvis:cli
    '''
)