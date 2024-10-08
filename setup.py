
from setuptools import setup, find_packages

setup(
    name='nsd_installment',
    version='0.0.1',
    description='Manage installment payments for sales orders.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",)
)
    