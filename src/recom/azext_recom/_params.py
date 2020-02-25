# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

# from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    # from find
    with self.argument_context('recom') as c:
        c.positional('cli_term', help='An Azure CLI command for which you need recommendation.')
