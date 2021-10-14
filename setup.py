import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="binodtharu-cli",
    version="0.4",
    author="Sayantan Das, Soumyadip Sarkar",
    author_email="sayantandas30011998@gmail.com, soumya997.sarkar@gmail.com",
    description="Binod",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soumya997/BinodTharu-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='binod',
    install_requires=[
      'wget',
      'tqdm',
    ],
    entry_points = {
        'console_scripts': [
            'binodcli = binodcli.__main__:main'
        ]
    }
)
