from setuptools import setup, find_packages

setup(
    name="netbox_dns_sd",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "jinja2"
    ]
)
