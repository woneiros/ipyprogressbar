import setuptools

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
	name='ipyprogressbar',
	version='1.0.2',
	description='Python-asynchronous progressbar widgets for use in Jupyter/IPython in conjunction with ipywidgets',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/WillahScott/ipyprogressbar',
	py_modules=['ipyprogressbar'],
	author='WillahScott',
	classifiers=[
	    'Intended Audience :: Developers',
	    'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
	    'License :: OSI Approved :: MIT License',
	    'Programming Language :: Python',
	    'Programming Language :: Python :: 2.7',
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.3',
	    'Programming Language :: Python :: 3.4',
	    'Programming Language :: Python :: 3.5',
	    'Framework :: Jupyter'
	],
	keywords='widget jupyter progressbar asynchronous',
	license='MIT',
	packages=setuptools.find_packages(),
	project_urls={
		'Say Thanks!': 'https://saythanks.io/to/WillahScott',
		'Bug Reports': 'https://github.com/WillahScott/ipyprogressbar/issues'
	}
)

