from setuptools import setup

version = '1.0'

setup(
	name='solidpy',
	version=version,
	description="Python client for the Solid API",
	long_description= open('README.rst').read(),
	keywords='error tracking, exception logging',
	author='Martin Rusev',
	author_email='martin@solidapp.io',
	url='https://github.com/martinrusev/solid-python',
	license='MIT',
	packages=['solidpy','solidpy.handlers'],
	package_dir={'solidpy':'solidpy'},
	zip_safe=False,
	install_requires=['requests',],
	classifiers=[
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
	],
) 
