# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kak_spell']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0',
 'path>=13.1.0,<14.0.0',
 'pyenchant==3.0.1',
 'pyxdg>=0.26,<0.27']

entry_points = \
{'console_scripts': ['kak-spell = kak_spell.cli:main']}

setup_kwargs = {
    'name': 'kak-spell',
    'version': '0.1.2',
    'description': 'PyEnchant wrapper for Kakoune',
    'long_description': '# kak-spell\n\nPyEnchant wrapper for Kakoune.\n\n## Installation\n\n\n1. Install the Enchant library, and the required dictionaries. See [PyEnchant documentation](https://pyenchant.github.io/pyenchant/install.html) for details.\n\n2. Install the `kak-spell` script, for instance with [pipx](https://pipxproject.github.io/pipx/):\n\n```\npipx install kak-spell\n```\n\n3. Install [plug.kak](https://github.com/andreyorst/plug.kak) and add the following lines in your `kakrc`:\n\n```kak\nplug "dmerejkowsky/kak-spell"\n\ndefine-command lint-on-save "hook buffer BufWritePre .* lint"```\n```\n\n\n4. (optional): declare a user mode and some mappings:\n\n```kak\ndeclare-user-mode kak-spell\nmap global user s \': enter-user-mode kak-spell<ret>\' -docstring \'enter spell user mode\'\nmap global kak-spell e \': kak-spell %opt{spell_lang}<ret>\' -docstring "enable spell checking"\nmap global kak-spell c \': kak-spell-clear<ret>\' -docstring \'clear spelling highlighters\'\nmap global kak-spell n \': kak-spell-next<ret>\' -docstring \'go to next spell error\'\nmap global kak-spell r \': kak-spell-replace<ret>\' -docstring \'suggest a list of replacements\'\nmap global kak-spell a \': kak-spell-add<ret>\' -docstring \'add the selection to the user dict\'\nmap global kak-spell x \': kak-spell-remove<ret>\' -docstring \'remove the selection from the user dict\'\n```\n\n\n\n## Discuss\n\nYou can discuss features of this plugin on [discuss.kakoune.com](https://discuss.kakoune.com/t/alternate-implementation-for-spell-checker/781).\n\nI\'d like to thank all the people who contributed code and ideas to make usage of this plugin easier.\n',
    'author': 'Dimitri Merejkowsky',
    'author_email': 'd.merej@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dmerejkowsky/kak-spell',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
