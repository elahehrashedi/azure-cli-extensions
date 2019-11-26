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
    """
    with self.command_group('recom') as g:
        g.custom_command('create', 'create_recom')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_recom')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_recom')


    with self.command_group('recom', is_preview=True):
        pass
    """
    # from find
    with self.command_group('') as g:
        g.custom_command('recom', 'process_query')
