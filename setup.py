from setuptools import setup

setup(
    name="to-do-py",
    version="0.1.0",
    py_modules=["main", "utils.interface_cli"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "to-do-py = main:cli",
        ],
    },
)
