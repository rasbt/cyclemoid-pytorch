# Sebastian Raschka 2022
# cyclemoid_pytorch
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: MIT

from os.path import realpath, dirname, join
from setuptools import setup, find_packages
import cyclemoid_pytorch

VERSION = cyclemoid_pytorch.__version__
PROJECT_ROOT = dirname(realpath(__file__))

REQUIREMENTS_FILE = join(PROJECT_ROOT, 'requirements.txt')

with open(REQUIREMENTS_FILE) as f:
    install_reqs = f.read().splitlines()

install_reqs.append('setuptools')


setup(name='cyclemoid_pytorch',
      version=VERSION,
      description='Cyclemoid implementation for PyTorch',
      author='Sebastian Raschka',
      author_email='mail@sebastianraschka.com',
      url='https://github.com/rasbt/cyclemoid_pytorch',
      packages=find_packages(),
      package_data={'': ['LICENSE.txt',
                         'README.md',
                         'requirements.txt']
                    },
      include_package_data=True,
      setup_requires=[],
      install_requires=install_reqs,
      license='MIT',
      platforms='any',
      keywords=['deep learning', 'pytorch', 'AI'],
      classifiers=[
             'License :: OSI Approved :: MIT License',
             'Development Status :: 5 - Production/Stable',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: POSIX',
             'Operating System :: Unix',
             'Operating System :: MacOS',
             'Programming Language :: Python :: 3.7',
             'Topic :: Scientific/Engineering',
             'Topic :: Scientific/Engineering :: Artificial Intelligence',
             'Topic :: Scientific/Engineering :: Information Analysis',
             'Topic :: Scientific/Engineering :: Image Recognition',
      ],
      long_description_content_type='text/markdown',
      long_description="""

Library implementing the core utilities for the
Cyclemoid activation function.
""")
