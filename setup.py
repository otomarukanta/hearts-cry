from setuptools import setup, find_packages

setup(
    name='heartscry',
    version='0.0.1',
    description='Hearts cry',
    author='otomarukanta',
    author_email='kanta208@gmail.com',
    url='http://otomarukanta.com/',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      heartscry_cmd = heartscry.cmd:main
      """
    )
