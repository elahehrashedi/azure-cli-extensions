# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# from azure.cli.core.commands import CliCommandType
# from azext_recom._client_factory import cf_recom


def load_command_table(self, _):

    # TODO: Add command type here
    # recom_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_recom)
    # from find
    with self.command_group('') as g:
        g.custom_command('recom', 'process_query')
