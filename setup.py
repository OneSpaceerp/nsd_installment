from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nsd_installment/__init__.py
from nsd_installment import __version__ as version

setup(
    name='nsd_installment',
    version=version,
    description='Manage installment payments for sales orders.',
    author='Nest Software Development',
    author_email='info@nsd-eg.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
