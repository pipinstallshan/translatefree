from setuptools import setup, find_packages

setup(
    name="translate_no_limit",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
        "undetected-chromedriver>=3.4.6",
        "fake-useragent>=1.2.0",
        "colorama>=0.4.6"
    ],
    author="Shahnoor",
    author_email="shahnr5889@example.com",
    description="A free library for translating text",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pipinstallshan/translate_no_limit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="3.8.0"
)
