from setuptools import setup

setup(name="systeminfo",
    version="0.01",
    description="System information for comp30670",
    url="",
    author="Conor Hopkins",
    author_email="conor.hopkins@ucdconnect.ie",
    licence="GPL3",
    packages=['systeminfo'],
    entry_points={
    'console_scripts':['comp30670_systeminfo=systeminfo.main:platform_specs']
    }
)

