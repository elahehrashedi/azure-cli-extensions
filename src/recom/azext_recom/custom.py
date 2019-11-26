# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import random
import json

# from knack.prompting import prompt
# from knack.log import get_logger
# logger = get_logger(__name__)
# from knack.util import CLIError

# WAIT_MESSAGE = ['I\'m an AI bot (learn more: aka.ms/aladdin); Let me see how I can help you...']

EXTENSION_NAME = 'recom'

RECOM_EXTENSION_PREFIX = 'Context.Default.Extension.Recom.'

RECOM_TABLE = 'C:/Elaheh/Recom_Branch/azure-cli-extensions/src/recom/azext_recom/data/top_recoms.json'
FAIL_TABLE = 'C:/Elaheh/Recom_Branch/azure-cli-extensions/src/recom/azext_recom/data/top_fails.json'
HELP_TABLE = 'C:/Elaheh/Recom_Branch/azure-cli-extensions/src/recom/azext_recom/data/help_dump.json'

"""
def create_recom(cmd, resource_group_name, recom_name, location=None, tags=None):
    raise CLIError('TODO: Implement `recom create`')


def list_recom(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `recom list`')


def update_recom(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance
"""


def process_query(cli_term):
    response = False
    # print(random.choice(WAIT_MESSAGE))

    with open(HELP_TABLE, encoding='utf8') as jsonfile:
        help_dump = json.load(jsonfile)

    with open(RECOM_TABLE, encoding='utf8') as jsonfile:
        recom_table = json.load(jsonfile)

    with open(FAIL_TABLE, encoding='utf8') as jsonfile:
        fail_table = json.load(jsonfile)

    # remove placeholders and values and sort the parameters
    command = get_parent_command_for_example(help_dump, cli_term)
    # print(command)
    # if command is not valid
    if command is None:
        print("\nSorry! this command is unknown [" + cli_term + "].")
        response = True
    else:
        sorted_params = get_sorted_param_list(help_dump, command, cli_term)
        key = " ".join([command] + sorted_params).strip()
        # print(key)
        if key in recom_table:
            print("\nHere are the most succesful commands to use after [" + cli_term + "] is failed: \n")
            for item in recom_table[key]['recoms']:
                print("az " + item[0])
        else:
            if key in fail_table:
                if len(sorted_params) != 0:
                    print("\nHere are the most succesful commands to use after [" + cli_term + "] is failed: \n")
                    for item in fail_table[key]['recoms']:
                        print("az " + item[0])
                    else:
                        # call Find API
            else:
                print("\nSorry I am not able to help with [" + cli_term + "].")
        response = True

    return response


def get_sorted_param_list(help_dump, command, example_command):
    """ convert the list of parameters to a sorted list of standardize parameters

    Attributes:
        command (str): the command
        example_command (str): the commands and its parameters
    output:
        paramset (list(str)): the sorted list of standard parameters
    """
    params = []
    param_set = set()

    terms = example_command.split()
    for item in terms:
        if item.startswith('-'):
            params += [item]

    # standardize the parameter
    for param in params:
        standard_param = get_standard_form_for_parameter(help_dump, command, param)
        param_set.add(standard_param)

    # sort the params and return the list
    return sorted(param_set)


def get_standard_form_for_parameter(help_dump, command, parameter):
    long_parameter = parameter
    for command_parameter in help_dump[command]['parameters']:
        if parameter == command_parameter or parameter in help_dump[command]['parameters'][command_parameter]['name']:
            long_parameter = command_parameter
            break

    return long_parameter


def get_parent_command_for_example(help_dump, example_command):
    commands = help_dump.keys()
    for command in sorted(commands, reverse=True):
        if example_command.startswith('az ' + command):
            return command

    return None
