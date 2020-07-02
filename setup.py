from setuptools import setup, find_packages


setup(
    name="youtube-scraper",
    version="1.0.3",
    description=("Provide information for youtube related metadata"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="youtube scraper meta",
    author="Jon Robison",
    author_email="narfman0@gmail.com",
    url="https://github.com/narfman0/youtube-scraper",
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    py_modules=["youtube_scraper.scraper"],
    zip_safe=True,
    install_requires=["beautifulsoup4", "requests"],
    test_suite="tests",
)
