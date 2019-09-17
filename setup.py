import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="prob-book",
    version="0.1",
    scripts=["prob-book"],
    author="Tom Gray",
    description="Interactive terminal and jupyter notebook kernel for probability calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TomJamesGray/prob-book",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "lark_parser",
        "ipykernel",
        "matplotlib",
        "numpy"
    ]
)