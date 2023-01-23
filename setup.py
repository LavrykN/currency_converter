import setuptools

setuptools.setup(
    name="currency",
    version="0.0.1",
    author="Nazar Lavryk",
    author_email="nazar.lavrik9@gmail.com",
    long_description_content_type="text/markdown",
    url="https://github.com/LavrykN/currency_converter",
    project_urls={
        "Bug Tracker": "https://github.com/LavrykN/currency_converter/issues"
    },
    license="MIT",
    packages=["currency"],
    install_requires=["requests"],
)
