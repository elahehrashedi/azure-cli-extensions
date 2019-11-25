# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from knack.help_files import helps

helps['ask'] = """
    type: command
    short-summary: I'm an AI robot, my advice is based on our Azure documentation as well as the usage patterns of Azure CLI and Azure ARM users. Using me improves Azure products and documentation.
    examples:
        - name: Give me any Azure CLI command that has failed recently and I’ll show the most used commands and parameters.
          text: |
            az ask 'az [command]' : az find 'az ad user list --output --query'
"""


class AskCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType

        process_query_custom = CliCommandType(
            operations_tmpl='azext_ask.custom#{}')
        super(AskCommandsLoader, self).__init__(
            cli_ctx=cli_ctx, custom_command_type=process_query_custom)

    def load_command_table(self, _):
        with self.command_group('') as g:
            g.custom_command('ask', 'process_query')
        return self.command_table

    def load_arguments(self, _):
        with self.argument_context('ask') as c:
            c.positional('cli_term', help='An Azure CLI command for which you need recommendation.')


COMMAND_LOADER_CLS = AskCommandsLoader