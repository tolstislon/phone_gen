from pathlib import Path

from setuptools import find_packages, setup

readme = Path(".", "README.md").absolute()
changelog = Path(".", "CHANGELOG.md").absolute()
with readme.open("r", encoding="utf-8") as file:
    long_description = file.read()
with changelog.open("r", encoding="utf-8") as file:
    long_description += file.read()

setup(
    name="phone_gen",
    packages=find_packages(exclude=("tests", "dev_tools")),
    url="https://github.com/tolstislon/phone-gen",
    license="MIT License",
    author="tolstislon",
    author_email="tolstislon@gmail.com",
    description="International phone number generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='2.0.11',
    entry_points={
        "console_scripts": ["phone-gen=phone_gen.cli:main"],
    },
    python_requires=">=3.5",
    include_package_data=True,
    keywords=["testing", "test-data", "phone-number", "phone"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
        "Topic :: Communications :: Telephony",
    ],
)
