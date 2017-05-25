from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='dream-server',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='A server for the \'dream\' project.',
      long_description=readme,
      author='Chandler Watson',
      author_email='watson@facni.com',
      url='https://github.com/useanalias/dream',
      license=license,
      py_modules=['dream_server'],
      scripts=['bin/dreamserver']
)
