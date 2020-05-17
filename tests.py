#   @copyright: 2020 by Pauli Rikula
#   @license: MIT <http://www.opensource.org/licenses/mit-license.php>



if __name__ == '__main__':
    import doctest
    import inverse_spectrogram
    import os

    # by importing these here, there might be some import errors left..
    globs = {
        'inverse_spectrogram': inverse_spectrogram.inverse_spectrogram,
    }
    os.chdir('./inverse_spectrogram')
    doctest.testfile(filename="inverse_spectrogram.py", module_relative=True, package=inverse_spectrogram, globs=globs)
    doctest.testfile(filename="__init__.py", module_relative=True, package=inverse_spectrogram, globs=globs)
