import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="google-translate-namdevel",
    version="0.0.1",
    author="namdevel",
    author_email="namdevel@gmail.com",
    description="(Unofficial) Googletrans: Free and Unlimited Google translate API for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" https://github.com/namdevel/google-translate",
    project_urls={
        "Bug Tracker": " https://github.com/namdevel/google-translate/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)