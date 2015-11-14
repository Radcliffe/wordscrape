from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='wordscrape',
      version='0.3',
      description='Extract data from forms in Microsoft Word documents.',
      url='http://github.com/Radcliffe/wordscrape',
      author='David Radcliffe',
      author_email='dradcliffe@gmail.com',
      license='MIT',
      packages=['wordscrape'],
      install_requires=[
        'lxml',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)