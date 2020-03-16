# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['splink']

package_data = \
{'': ['*'], 'splink': ['files/*']}

install_requires = \
['jsonschema>=3.2,<4.0']

setup_kwargs = {
    'name': 'splink',
    'version': '0.1.5',
    'description': "[Beta]: Implementation in Apache Spark of the EM algorithm to estimate parameters of Fellegi-Sunter's canonical model of record linkage.",
    'long_description': "[![Coverage Status](https://coveralls.io/repos/github/moj-analytical-services/splink/badge.svg?branch=dev)](https://coveralls.io/github/moj-analytical-services/splink?branch=master)\n![issues-status](https://img.shields.io/github/issues-raw/moj-analytical-services/splink)\n![python-version-dependency](https://img.shields.io/badge/python-%3E%3D3.6-blue)\n\n\n# splink: Probabalistic record linkage at scale\n\nWARNING:  Splink is is currently in beta testing.  Please feel free to try it, but note this software is not fully tested, and the interface is likely to continue to change.\n\n`splink` implements Fellegi-Sunter's canonical model of record linkage in Apache Spark, including EM algorithm to estimate parameters of the model.\n\nThe aims of `splink` are to:\n\n- Work at much greater scale than current open source implementations (100 million records +).\n\n- Get results faster than current open source implementations - with runtimes of less than an hour.\n\n- Have a highly transparent methodology, so the match scores can be easily explained both graphically and in words\n\n- Have accuracy similar to some of the best alternatives\n\n## Installation\n\n`splink` is a Python package.  It uses the Spark Python API to execute data linking jobs in a Spark cluster.  It has been tested in Apache Spark 2.3 and 2.4.\n\nInstall splink using\n\n`pip install splink`\n\n## Interactive demo\n\nYou can run demos of `splink` in an interactive Jupyter notebook by clicking the button below:\n\n[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/moj-analytical-services/splink_demos/master?urlpath=lab/tree/index.ipynb)\n\n## Documentation\n\nThe best documentation is currently a series of demonstrations notebooks in the [splink_demos](https://github.com/moj-analytical-services/splink_demos) repo.\n\nWe also provide an interactive `splink` settings editor and example settings [here](https://moj-analytical-services.github.io/splink_settings_editor/)\n\nThe statistical model behind `splink` is the same as that used in the R [fastLink package](https://github.com/kosukeimai/fastLink).  Accompanying the fastLink package is an [academic paper](http://imai.fas.harvard.edu/research/files/linkage.pdf) that describes this model.  This is the best place to start for users wanting to understand the theory about how `splink` works.\n\n## Video intro\n\nYou can find a short video introducing `splink` and running though an introductory demo [here](https://www.youtube.com/watch?v=_8lV2Lbd6Xs&feature=youtu.be&t=1295).\n\n## Acknowledgements\n\nWe are grateful to [ADR UK](https://www.adruk.org/) (Administrative Data Research UK) for providing funding for this work as part of the [Data First](https://www.adruk.org/our-work/browse-all-projects/data-first-harnessing-the-potential-of-linked-administrative-data-for-the-justice-system-169/) project.",
    'author': 'Robin Linacre',
    'author_email': 'robinlinacre@hotmail.com',
    'url': 'https://github.com/moj-analytical-services/splink',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
