from setuptools import setup, find_packages

setup(
  name = "mkpkg",
  version = "0.1",
  packages = find_packages(),
  scripts = ["mkpkg",],
  author = "Technigami",
  author_email = "hello@technigami.com",
  description = "This is a simple script we wrote to simply make a new python package",
  license = "GNU",
  keywords = "script, cli tools, tools",
  url = "http://technigami.com/mkpkg"

)

