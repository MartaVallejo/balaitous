from setuptools import setup, find_packages

setup(name='balaitous',
      author='Simon Jégou',
      version='1.0',
      description='Codebase to run the Balaitous model',
      long_description='Codebase to run the Balaitous model, more information at https://github.com/SimJeg/balaitous/blob/master/README.md',
      packages=find_packages(),
      license ='MIT',
      install_requires=[
          'numpy',
          'SimpleITK',
          'scikit-image',
          'torch',
          'torchvision',
          'lungmask @ git+https://git@github.com/JoHof/lungmask@v0.2.4',
      ],
       entry_points ={'console_scripts': ['balaitous = balaitous.cli:cli']})
