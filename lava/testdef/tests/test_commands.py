# Copyright (C) 2013 Linaro Limited
#
# Author: Milo Casagrande <milo.casagrande@linaro.org>
#
# This file is part of lava-tool.
#
# lava-tool is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# lava-tool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with lava-tool.  If not, see <http://www.gnu.org/licenses/>.

"""
Tests for lava.testdef.commands.
"""

import os
import tempfile
import yaml

from mock import (
    MagicMock,
    patch,
)

from lava.config import InteractiveCache
from lava.helper.tests.helper_test import HelperTest
from lava.testdef.commands import (
    new,
)
from lava.tool.errors import CommandError


class NewCommandTest(HelperTest):

    """Class for the lava.testdef new command tests."""

    def setUp(self):
        super(NewCommandTest, self).setUp()
        self.file_name = "fake_testdef.yaml"
        self.file_path = os.path.join(tempfile.gettempdir(), self.file_name)
        self.args.FILE = self.file_path

        self.temp_yaml = tempfile.NamedTemporaryFile(suffix=".yaml",
                                                     delete=False)

        self.config_file = tempfile.NamedTemporaryFile(delete=False)
        self.config = InteractiveCache()
        self.config.save = MagicMock()
        self.config.config_file = self.config_file.name
        # Patch class raw_input, start it, and stop it on tearDown.
        self.patcher1 = patch("lava.parameter.raw_input", create=True)
        self.mocked_raw_input = self.patcher1.start()

    def tearDown(self):
        super(NewCommandTest, self).tearDown()
        if os.path.isfile(self.file_path):
            os.unlink(self.file_path)
        os.unlink(self.config_file.name)
        os.unlink(self.temp_yaml.name)
        self.patcher1.stop()

    def test_register_arguments(self):
        # Make sure that the parser add_argument is called and we have the
        # correct argument.
        new_command = new(self.parser, self.args)
        new_command.register_arguments(self.parser)

        # Make sure we do not forget about this test.
        self.assertEqual(2, len(self.parser.method_calls))

        _, args, _ = self.parser.method_calls[0]
        self.assertIn("--non-interactive", args)

        _, args, _ = self.parser.method_calls[1]
        self.assertIn("FILE", args)

    def test_invoke_0(self):
        # Test that passing a file on the command line, it is created on the
        # file system.
        self.mocked_raw_input.return_value = "\n"
        new_command = new(self.parser, self.args)
        new_command.config = self.config
        new_command.invoke()
        self.assertTrue(os.path.exists(self.file_path))

    def test_invoke_1(self):
        # Test that when passing an already existing file, an exception is
        # thrown.
        self.args.FILE = self.temp_yaml.name
        new_command = new(self.parser, self.args)
        new_command.config = self.config
        self.assertRaises(CommandError, new_command.invoke)

    def test_invoke_2(self):
        # Tests that when adding a new test definition and writing it to file
        # a correct YAML structure is created.
        self.mocked_raw_input.return_value = "\n"
        new_command = new(self.parser, self.args)
        new_command.config = self.config
        new_command.invoke()
        expected = {'run': {'steps': ["./mytest.sh"]},
                    'metadata': {
                        'environment': ['lava_test_shell'],
                        'format': 'Lava-Test Test Definition 1.0',
                        'version': '1.0',
                        'description': '',
                        'name': ''},
                    'parse': {
                        'pattern':
                        '^\\s*(?P<test_case_id>\\w+)=(?P<result>\\w+)\\s*$'
                    },
                    }
        obtained = None
        with open(self.file_path, 'r') as read_file:
            obtained = yaml.load(read_file)
        self.assertEqual(expected, obtained)

    def test_invoke_3(self):
        # Tests that when adding a new test definition and writing it to a file
        # in a directory withour permissions, exception is raised.
        self.args.FILE = "/test_file.yaml"
        self.mocked_raw_input.return_value = "\n"
        new_command = new(self.parser, self.args)
        new_command.config = self.config
        self.assertRaises(CommandError, new_command.invoke)
        self.assertFalse(os.path.exists(self.args.FILE))

    def test_invoke_4(self):
        # Tests that when passing values for the "steps" ListParameter, we get
        # back the correct data structure.
        self.mocked_raw_input.side_effect = ["foo", "\n", "\n", "\n", "\n",
                                             "\n"]
        new_command = new(self.parser, self.args)
        new_command.config = self.config
        new_command.invoke()
        expected = {'run': {'steps': ["./mytest.sh"]},
                    'metadata': {
                        'environment': ['lava_test_shell'],
                        'format': 'Lava-Test Test Definition 1.0',
                        'version': '1.0',
                        'description': '',
                        'name': 'foo'
                    },
                    'parse': {
                        'pattern':
                        '^\\s*(?P<test_case_id>\\w+)=(?P<result>\\w+)\\s*$'
                    },
                    }
        obtained = None
        with open(self.file_path, 'r') as read_file:
            obtained = yaml.load(read_file)
        self.assertEqual(expected, obtained)
