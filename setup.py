import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    require = fh.readlines()
require = [x.strip() for x in require]

setuptools.setup(
    name="matSankey",
    version="0.2.2",
    description="Make Simple Sankey Diagrams with Matplotlib and Seaborn",
    long_description=long_description,
    license='GNU General Public License v3.0',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=require
)
