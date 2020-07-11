import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="nhk-easy",
    version="0.0.1",
    url="https://github.com/TianyiShi2001/nhk-easy",
    license="MIT",
    author="Tianyi Shi",
    author_email="ShiTianyi2001@outlook.com",
    description="Download today's news on https://www3.nhk.or.jp/news/easy/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(exclude=("tests",)),
    install_requires=["requests", "lxml"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["nhk=reader.__main__:main",]},
)
