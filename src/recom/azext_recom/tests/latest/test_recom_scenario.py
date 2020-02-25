# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

from azext_recom.custom import process_query


class RecomScenarioTest(unittest.TestCase):

    def test_process_query(self):
        response = process_query("az container attach --container-name --name --resource-group")
        # response = process_query("az aks browse --name --resource-group")
        # response = process_query("az aks")
        self.assertEqual(True, response)


if __name__ == '__main__':
    unittest.main()
