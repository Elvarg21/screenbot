from setuptools import setup, find_packages

with open('screenbot/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")

setup(
    name='screenbot',
    version=version,
    description='Your best friend and ',
    url='',
    author='Elvarg21',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'pyautogui',
        'pynput'
    ],
    dependency_links=[
    ],
    zip_safe=False
)
