#! /usr/bin/env python

from setuptools import setup, find_packages
import versioneer

setup (
    name = "rrmapper",
    version = versioneer.get_version (),
    description = "Ricochet Robots map generator",
    long_description = "Variant map generator system for the Ricochet Robots game by Alex Randolph",
    cmdclass = versioneer.get_cmdclass (),
    classifiers = [],
    keywords = "ricochet robots, game files",
    author = "J C Lawrence",
    author_email = "claw@kanga.nu",
    url = "https://github.com/clearclaw/rrmapper",
    license = "Creative Commons Attribution-ShareAlike 3.0 Unported",
    packages = find_packages (exclude = ["tests",]),
    include_package_data = True,
    zip_safe = False,
    install_requires = [line.strip ()
                        for line in file ("requirements.txt").readlines ()
                    ],
  entry_points = {
    "console_scripts": [
      "rrmapper = rrmapper.main:main",
      ],
    },
  )
