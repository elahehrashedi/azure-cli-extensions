# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_recom._help import helps  # pylint: disable=unused-import


class RecomCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_recom._client_factory import cf_recom
        recom_custom = CliCommandType(
            operations_tmpl='azext_recom.custom#{}',
            client_factory=cf_recom)
        super(RecomCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                  custom_command_type=recom_custom)

    def load_command_table(self, args):
        from azext_recom.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_recom._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = RecomCommandsLoader
