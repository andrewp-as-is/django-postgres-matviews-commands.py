import setuptools

setuptools.setup(
    name='django-postgres-matviews-commands',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
