#   @copyright: 2020 by Pauli Rikula
#   @license: MIT <http://www.opensource.org/licenses/mit-license.php>


from setuptools import setup
import inverse_spectrogram

with open('README.md', 'r') as readme_file:
    README = readme_file.read()

setup(
    name='pyhon-inverse-spectrogram',
    version='0.0.2',
    description='Inverse spectogram for scipy.signal.spectrogram',
    long_description=README,
    license="MIT",
    author="Pauli Rikula",
    url='https://github.com/kummahiih/python-inverse-spectrogram',
    packages=['inverse_spectrogram'],
    python_requires='~=3.8',
    install_requires=[
          'numpy>=1.18.4',
          'scipy>=1.4.1'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8']
)
    