from pip._internal.req import parse_requirements
from pip._internal.download import PipSession
from setuptools import setup, find_packages
from youtube_scraper import __version__ as version

requirements = [
    str(req.req) for req in parse_requirements('requirements.txt', session=PipSession())
]

setup(
    name='youtube-scraper',
    version=version,
    description=('Provide information for youtube related metadata'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='youtube scraper meta',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/youtube-scraper',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['youtube_scraper.scraper'],
    zip_safe=True,
    install_requires=requirements,
    test_suite='tests',
)
