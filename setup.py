import os
from distutils.core import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name="nepal_geonode",
    version="0.1",
    author="",
    author_email="",
    description="Nepal GeoNode, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="nepal_geonode geonode django",
    url='https://github.com/GFDRR/Nepal-Geonode.git',
    packages=['nepal_geonode', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
)
