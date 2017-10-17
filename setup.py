from setuptools import setup
from setuptools import find_packages

setup(
	name = 'Admire',
	version = '1.0.0',
	packages = find_packages(),

	install_requires = ['requests>=2.18.2'],

	author = 'Avlyssna',
	author_email = 'avlyssna@gmail.com',
	description = 'An intuitive reCAPTCHA interface.',
	license = 'MIT',
	keywords = 'reCAPTCHA CAPTCHA'
	url = 'https://github.com/Avlyssna/Admire'
)
