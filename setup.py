import setuptools

# todo create a package
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="3D-captcha",
    version="0.0.1",
    author="Roy Levy",
    author_email="roiwow2@gmail.com",
    description="Generate a smart test with 3D for Captcha validation ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roylevy1/3D-Captcha",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: gpl-3.0",
        "Operating System :: OS Independent",
    ],
)