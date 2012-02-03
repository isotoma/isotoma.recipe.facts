from setuptools import setup, find_packages

version = '0.0.5'

setup(
    name = 'isotoma.recipe.facts',
    version = version,
    description = "A recipe to provide facts about the context a buildout is running in",
    long_description = open("README.rst").read() + "\n" + open("CHANGES.txt").read(),
    classifiers = [
        "Framework :: Buildout",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords = "buildout facts",
    author = "John Carr",
    author_email = "john.carr@isotoma.com",
    license="Apache Software License",
    packages = find_packages(exclude=['ez_setup']),
    package_data = {
        '': ['README.rst', 'CHANGES.txt'],
    },
    namespace_packages = ['isotoma', 'isotoma.recipe'],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'zc.buildout',
    ],
    entry_points = {
        "zc.buildout": [
            "default = isotoma.recipe.facts:Facts",
        ],
    }
)

