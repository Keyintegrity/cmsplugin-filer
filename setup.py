from setuptools import setup, find_packages

from cmsplugin_filer_file import __version__

setup(
    name="cmsplugin-filer",
    version=__version__,
    url='https://github.com/pawelmarkowski/cmsplugin-filer',
    license='BSD',
    description="django-cms plugins for django-filer",
    long_description=open('README.rst').read(),
    author='Stefan Foulis',
    author_email='stefan.foulis@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django>=2.2,<4.0",
        "django-appconf>=1.0.4,<2.0",
        "django-cms>=3.7,<4.0",
        "django-filer>=1.5.0,<3.0",
        "django-sekizai>=1.0.0,<5.0",
        "djangocms-attributes-field>=1.1.0,<3.0",
        "easy_thumbnails>=2.6.0,<3.0",
    ],
    include_package_data=True,
    zip_safe=False,
)
