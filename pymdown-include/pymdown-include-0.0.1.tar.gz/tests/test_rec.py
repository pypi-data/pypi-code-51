# Copyright 2020 Jacques Supcik
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import unittest
from pathlib import Path

import markdown

from pymdown_include import PymdownInclude


class RecursiveTests(unittest.TestCase):

    def setUp(self):
        self.md = markdown.Markdown(
            extensions=[PymdownInclude(SEARCH_PATH=[Path(__file__).parent])]
        )

    def test_rec(self):

        MD = """
            A {!rec.md!} B
        """

        HTML = """
            <p>A X line 1
            line 2
            line 3 Y B</p>
        """

        self.assertEqual(self.md.convert(
            inspect.cleandoc(MD)), inspect.cleandoc(HTML))

if __name__ == '__main__':
    unittest.main()
