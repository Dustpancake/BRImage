from setuptools import setup, Extension
import os

algorithms = Extension(
	'algorithms', 
	sources=[
		os.path.join('BRImage', 'clib', 'br_algorithms.c'),
		os.path.join('BRImage', 'clib', 'freqmod.c')
	],
	include_dirs = [
		os.path.join('BRImage', 'clib')
	]
)

with open('README.md', 'r') as f:
	long_description=f.read();

setup(
	name='BRImage',
	version='0.1.0',
	description='Glitch ART Toolkit mimicking CRT monitor defects.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	author='Dustpancake',
	url='https://github.com/Dustpancake/BRImage',
	packages=[
		'BRImage', 
		'BRImage.glitchcore', 
		'BRImage.overlays',
		'BRImage.overlays.structures'
	],
	install_requires=[
		'numpy==1.18.2',
		'scipy==1.4.1',
		'matplotlib==3.2.1',
		'Pillow==7.1.1'
	],
	ext_package='__brimage_lib',
	ext_modules=[
		algorithms
	],
	 classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
	],
	zip_safe=False
)