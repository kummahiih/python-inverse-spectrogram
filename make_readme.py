#   @copyright: 2020 by Pauli Rikula
#   @license: MIT <http://www.opensource.org/licenses/mit-license.php>

import inverse_spectrogram

README =  "# pyhon-inverse-spectrogram" + "\n"
README += inverse_spectrogram.__doc__
README += '\n## inverse_spectrogram(f, t, Sxx, fs)'+ "\n" + inverse_spectrogram.inverse_spectrogram.__doc__


with open('README.md', 'wt') as readme_file:
    readme_file.write(README)