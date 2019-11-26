# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

from azext_recom.custom import process_query


class RecomScenarioTest(unittest.TestCase):

    def test_process_query(self):
        response = process_query("az container attach --container-name --name --resource-group")
        self.assertEqual(True, response)


if __name__ == '__main__':
    unittest.main()

'''
import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class RecomScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_recom')
    def test_recom(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

        self.cmd('recom create -g {rg} -n {name} --tags foo=doo', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}')
        ])
        self.cmd('recom update -g {rg} -n {name} --tags foo=boo', checks=[
            self.check('tags.foo', 'boo')
        ])
        count = len(self.cmd('recom list').get_output_in_json())
        self.cmd('recom show - {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'boo')
        ])
        self.cmd('recom delete -g {rg} -n {name}')
        final_count = len(self.cmd('recom list').get_output_in_json())
        self.assertTrue(final_count, count - 1)
'''
