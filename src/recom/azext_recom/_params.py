# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

# from knack.arguments import CLIArgumentType


def load_arguments(self, _):
    """
    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group
    recom_name_type = CLIArgumentType(options_list='--recom-name-name', help='Name of the Recom.', id_part='name')

    with self.argument_context('recom') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('recom_name', recom_name_type, options_list=['--name', '-n'])

    with self.argument_context('recom list') as c:
        c.argument('recom_name', recom_name_type, id_part=None)
    """
    # from find
    with self.argument_context('recom') as c:
        c.positional('cli_term', help='An Azure CLI command for which you need recommendation.')
