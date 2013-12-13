from setuptools import setup, find_packages
import os

version = '1.0.2dev'

setup(name='silva.pageactions.pdf',
      version=version,
      description="Create a PDF out of the current page in Silva CMS",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silva page actions pdf',
      author='Infrae',
      author_email='info@infrae.com',
      url='https://github.com/silvacms/silva.pageactions.pdf',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silva', 'silva.pageactions'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'five.grok',
        'grokcore.chameleon',
        'setuptools',
        'silva.core.views',
        'silva.pageactions.base',
        'silva.pageactions.printfriendly',
        'zope.component',
        ],
      )
