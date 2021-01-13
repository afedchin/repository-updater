"Home Assistant add-ons repository updater setup."
from setuptools import setup, find_packages

from repositoryupdater import (
    __author__,
    __email__,
    __license__,
    __url__,
    __download__,
    APP_NAME,
    APP_VERSION,
    APP_DESCRIPTION,
)

setup(
    name=APP_NAME,
    version=APP_VERSION,
    author=__author__,
    author_email=__email__,
    description=APP_DESCRIPTION.split("\n")[0],
    long_description=APP_DESCRIPTION,
    license=__license__,
    url=__url__,
    download_url=__download__,
    keywords=[
        "addons",
        "repository",
        "home assistant",
        "home-assistant",
        "add-ons",
        "frenck",
    ],
    platforms="any",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=[
        "click==7.1.2",
        "crayons==0.4.0",
        "emoji==0.6.0",
        "GitPython==3.1.12",
        "Jinja2==2.11.2",
        "PyGithub==1.54.1",
        "python-dateutil==2.8.1",
        "PyYAML==5.3.1",
        "semver==2.13.0",
    ],
    entry_points="""
        [console_scripts]
            repository-updater=repositoryupdater.cli:repository_updater
            repository-updater-git-askpass=repositoryupdater.cli:git_askpass
    """,
)
